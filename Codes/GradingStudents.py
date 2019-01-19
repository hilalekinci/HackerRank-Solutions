#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#

def findNextMultiple5(num):
    while(num%5 != 0):
        num +=1
    return num



def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        else:
            m5 = findNextMultiple5(grades[i])
            if (m5 - grades[i]) < 3:
                grades[i] = m5
    return grades

    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
