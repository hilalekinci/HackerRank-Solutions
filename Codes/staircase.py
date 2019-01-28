#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        j = i
        while n - i -1 != 0:
            print(" ", end ="")
            i += 1
       
        while j+1:
            print("#", end ="")
            j -= 1
        print("")



if __name__ == '__main__':
    n = int(input())

    staircase(n)
