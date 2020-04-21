# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d1 = {}
    for i in range(len(s1)):
        if(s1[i] in d1.keys()):
            d1[s1[i]] += 1
        else:
            d1[s1[i]] = 1

    d2 = {}
    for i in range(len(s2)):
        if(s2[i] in d2.keys()):
            d2[s2[i]] += 1
        else:
            d2[s2[i]] = 1

    for i in d1.keys():
        if(i in d2.keys()):
            return "YES"
        continue
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
