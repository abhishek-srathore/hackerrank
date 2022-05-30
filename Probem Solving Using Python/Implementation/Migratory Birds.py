#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    d = {}
    mx = 0
    for i in arr:
        d[i] = d.get(i, 0)+1
        if d[i] > mx:
            mx = d[i]
    ans = 9999999999999999999999999999999999999
    for i in d:
        if d[i]==mx:
            if i<ans:
                ans = i
    return ans


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
