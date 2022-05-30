#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if s[0] == " ":
        stf = " "
    else:
        stf = s[0].upper() 
    for i in range(1,len(s)):
        if s[i-1] == ' ':
            if s[i].isalpha():
                stf = stf + s[i].upper()
            else:
                stf = stf + s[i]
        
            
        else:
            stf = stf+ s[i] 
    return(stf)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
