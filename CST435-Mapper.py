#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        numbers = [int(x) for x in line.strip().split()]
        print("Unsorted Data:", numbers)
        for num in numbers:
            print(f'1\t{num}')

if __name__ == '__main__':
    mapper()