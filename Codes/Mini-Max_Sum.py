#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minmaxList = []

    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if i == j:
                continue
            sum += arr[j]
        minmaxList.append(sum)
        
    print( min(minmaxList), max(minmaxList))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
