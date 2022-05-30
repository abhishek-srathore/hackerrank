#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    arr = s.rstrip().split(":")
    if arr[0] !=  "12":
        if (arr[-1][-1:-3:-1]) == "MP" :
            H = 12+ int(arr[0])
            arr[0] = str(H)
    
    else:
        if (arr[-1][-1:-3:-1]) == "MP" :
            arr[0] = "12"
        else:
            arr[0] = "00"
    arr[-1] = arr[-1] [:2]
    return ":".join(arr)
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
