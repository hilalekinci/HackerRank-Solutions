#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if "PM" in s:
        s = s.replace("PM", "")
        s = s.split(":")
        if s[0] != "12":  # Check the hour whether it is not 12
            s[0] =  str(int(s[0]) + 12) 
        
        s = ":".join(s)
        return s
    elif "AM" in s:
        s = s.replace("AM", "")
        s = s.split(":")
        if s[0] == "12": # Check the hour whether it is 12
            s[0] = "00"
        s = ":".join(s)
        return s


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    f.write(result + '\n')

    f.close()
