#!/usr/bin/env python3
import sys
import time

def reducer():
    start_time = time.time()  # Start timing
    numbers = []
    for line in sys.stdin:
        if line.startswith("Unsorted Data:"):
            print(line.strip())
            continue
        try:
            key, value = line.strip().split('\t')
            numbers.append(int(value))
        except ValueError:
            continue
    
    numbers.sort()
    print(f'Sorted Data: {numbers}')
    end_time = time.time()  # End timing
    print(f"Reducer Execution Time: {end_time - start_time:.6f} seconds", file=sys.stderr)

if __name__ == '__main__':
    reducer()
