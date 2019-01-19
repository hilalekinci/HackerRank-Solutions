#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar, ar_count):
    sum =0
    for i in range(ar_count):
        sum += ar[i]
    return sum

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar, ar_count)

    fptr.write(str(result) + '\n')

    fptr.close()
