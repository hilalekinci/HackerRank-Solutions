#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    PlusNum = 0
    MinusNum = 0
    ZeroNum = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            ZeroNum += 1
        elif arr[i] > 0:
            PlusNum += 1
        else:
            MinusNum +=1
    print(round(PlusNum/len(arr),6))
    print(round(MinusNum/len(arr),6))
    print(round(ZeroNum/len(arr),6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
