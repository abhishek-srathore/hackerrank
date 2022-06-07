#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    if path[0]=="D":
        sm = -1
        coun = 1
    else:
        sm = 1
        coun = 0
    for i in range(1, steps-1):
        if path[i] == "D":
            sm = sm -1
        else:
            sm = sm+ 1
        
        print(sm)
        
        if sm ==0 and path[i+1] =="D":
            coun +=1
    return coun
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

