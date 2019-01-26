#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    AlicePoints = 0
    BobPoints = 0

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            AlicePoints += 1
        else:
            BobPoints += 1

    return AlicePoints , BobPoints


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
