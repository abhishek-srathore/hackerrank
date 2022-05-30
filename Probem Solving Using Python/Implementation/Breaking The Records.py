#!/bin/python3

import math
import os
import random
import re
import sys



def breakingRecords(scores):
    l = scores[0]
    x = scores[0]
    cl = 0
    cx = 0
    for i in scores:
        if i>x:
            x=i
            cx+=1
        if i< l:
            l=i
            cl += 1
    return cx,cl

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
