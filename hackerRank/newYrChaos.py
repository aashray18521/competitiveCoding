# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    bribe = 0
    for i in range(n):
        if(q[i] - (i+1) > 2):
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-2), i):
            if(q[j] > q[i]):
                bribe += 1
    print(bribe)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
