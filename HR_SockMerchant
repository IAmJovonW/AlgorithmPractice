#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colorMap = {}
    numOfPairs = 0
    for i in ar:
        if i in colorMap:
            colorMap[i] += 1
        else:
            colorMap[i] = 1
    
    for k in colorMap:
        colorMap[k] = colorMap[k]//2
        numOfPairs += colorMap[k]
    return numOfPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
