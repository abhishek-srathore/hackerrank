#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    n = len(candles)
    mx = 0
    count =0
    for i in candles:

        if i >= mx:
            if mx == i:
                count +=1
            else:
                mx = i
                count=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
