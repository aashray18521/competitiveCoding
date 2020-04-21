# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

def slideMask(arr):
    mask = []
    mask.append([1, 1, 1])
    mask.append([0, 1, 0])
    mask.append([1, 1, 1])
    res = 0
    for i in range(3):
        for j in range(3):
            res += arr[i][j] * mask[i][j]
    return res

# Complete the hourglassSum function below.
def hourglassSum(arr):
    finalz = -99999999
    # slide mask over array
    for i in range(4):
        for j in range(4):
            temp = []
            temp.append(arr[i][j:j+3]) 
            temp.append(arr[i+1][j:j+3]) 
            temp.append(arr[i+2][j:j+3])
            res = slideMask(temp)
            finalz = max(res, finalz)
    return finalz

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
