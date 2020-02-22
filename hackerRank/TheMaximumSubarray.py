#!/bin/python3

import math
import os
import random
import re
import sys

def subarray(arr, n):
    res = arr[0]
    curr = arr[0]
    for i in range(1, n):
        curr = max(curr+arr[i], arr[i])
        res = max(curr, res)
    return res

def subsequence(arr, n):
    res = arr[0]
    curr = arr[0]
    for i in range(1, n):
        curr = max(curr, arr[i]+curr)
        if(curr < arr[i]):
            curr = arr[i]
        res = max(curr, res)
    return res

# Complete the maxSubarray function below.
def maxSubarray(arr):
    res1 = subarray(arr, len(arr))
    res2 = subsequence(arr, len(arr))
    return [res1, res2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
