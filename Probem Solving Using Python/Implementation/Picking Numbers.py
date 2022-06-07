#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    a.sort()
    i = 1
    c =a[0]
    count_p = 1
    s = 0
    while i<len(a):
        if a[i] - c<=1:
            count_p +=1
        else:
            c= a[i]
            if count_p>s:
                s=count_p
            count_p = 1
        
        i +=1
    if s == 0:
        return count_p
    else:
        return s
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
