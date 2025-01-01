#!/usr/bin/env python3
import sys

def reducer():
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

if __name__ == '__main__':
    reducer()