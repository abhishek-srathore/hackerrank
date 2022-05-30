#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
        # Write your cod
        if p%2 !=0:
            page = p-1
        else:
            page = p

        if n%2 !=0:
            num = n-1
        else:
            num = n

        frwd_count= page//2
        bcwk_count = (num-page)//2
        
        return min(frwd_count, bcwk_count)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
