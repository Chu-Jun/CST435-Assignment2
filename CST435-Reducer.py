#!/usr/bin/env python3
import sys
import time

def reducer():
    start_time = time.time()  # Start timing
    numbers = []
    mapper_times = []

    for line in sys.stdin:
        if line.startswith("Unsorted Data:"):
            print(line.strip())
            continue
        try:
            key, value = line.strip().split('\t')
            if key == "MapperExecutionTime":
                mapper_times.append(float(value))
            else:
                 numbers.append(int(value))
        except ValueError:
            continue
    
    numbers.sort()
    print(f'Sorted Data: {numbers}')

    total_mapper_time = sum(mapper_times)
    print(f"Mapper Execution Time: {total_mapper_time:.6f} seconds")

    end_time = time.time()  # End timing
    print(f"Reducer Execution Time: {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    reducer()
