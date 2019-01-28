#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    st_apples = 0
    st_oranges = 0

    for i in range(len(apples)):
        if a + apples[i] >= s and a + apples[i] <= t:
            st_apples += 1

    for i in range(len(oranges)):
        if b + oranges[i] >= s and b + oranges[i] <= t:
            st_oranges += 1
    
    print(st_apples)
    print(st_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
