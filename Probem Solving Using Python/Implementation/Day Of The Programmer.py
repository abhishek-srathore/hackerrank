#!/bin/python3

import math
import os
import random
import re
import sys


def dayOfProgrammer(year):
    if year>1918:
        if year%4==0 and year%100 != 0 or year%400 ==0:
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    elif year <1918:
        if year%4==0 :
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    else:
        return "26.09.1918"
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
