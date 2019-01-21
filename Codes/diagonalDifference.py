#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(n,arr):
    PrimarySum = 0
    SecondarySum = 0
 
    for i in range(n):
        PrimarySum += arr[i][i]

    for j in range(n):
        SecondarySum += arr[j][n - j - 1]

    return abs(PrimarySum - SecondarySum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))


    result = diagonalDifference(n,arr)
    fptr.write(str(result) + '\n')
    fptr.close()
