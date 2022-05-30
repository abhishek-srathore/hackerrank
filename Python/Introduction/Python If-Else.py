#!/bin/python3

import math
import os
import random
import re


if __name__ == '__main__':
    n = int(input())
    if n%2==1:
        print ('Weird')
    elif n/2==2 or n/2==1:
      print('Not Weird')
    elif n/2>=3 and n/2<=10:
            print('Weird')
    elif n/2>10:
            print('Not Weird')
