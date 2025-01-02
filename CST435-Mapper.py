#!/usr/bin/env python3
import sys
import time

def mapper():
    start_time = time.time()  # Start timing
    for line in sys.stdin:
        numbers = [int(x) for x in line.strip().split()]
        print("Unsorted Data:", numbers)
        for num in numbers:
            print(f'1\t{num}')
    end_time = time.time()  # End timing
    print(f"Mapper Execution Time: {end_time - start_time:.6f} seconds", file=sys.stderr)

if __name__ == '__main__':
    mapper()
