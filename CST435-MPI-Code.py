from mpi4py import MPI
import numpy as np
import sys

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Read input data from the file in rank 0
if rank == 0:
    if len(sys.argv) < 2:
        print("Usage: mpiexec -n <num_processes> python mpi_merge_sort.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        data = list(map(int, file.read().split()))
    print(f"Unsorted data: {data}")  # Display the unsorted data
else:
    data = None

# Scatter data to all processes
data = comm.bcast(data, root=0)
chunk_size = len(data) // size
if rank == size - 1:  # Last process takes the remainder
    local_data = data[rank * chunk_size:]
else:
    local_data = data[rank * chunk_size:(rank + 1) * chunk_size]

# Sort the local chunk
local_sorted = merge_sort(local_data)

# Gather sorted chunks at root
sorted_chunks = comm.gather(local_sorted, root=0)

# Merge all sorted chunks at root
if rank == 0:
    sorted_data = []
    for chunk in sorted_chunks:
        sorted_data = merge(sorted_data, chunk)
    print(f"Sorted data: {sorted_data}")  # Display the sorted data
