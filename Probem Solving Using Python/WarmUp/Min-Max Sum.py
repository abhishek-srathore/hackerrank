#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sum = 0
    mx = -999999999999999999999999999999
    mn = 9999999999999999999999999999999
    for i in arr:
        sum += i
        if i>mx:
            mx = i
        if i<mn:
            mn = i
    print((sum- mx),(sum - mn))
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
