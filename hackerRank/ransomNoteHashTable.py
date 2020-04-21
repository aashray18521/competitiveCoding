# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print(len(note))
    # print(len(magazine))
    # if(len(note) > len(magazine)):
    #     print("No")
    #     return 

    dM = {}
    for i in range(len(magazine)):
        if(magazine[i] in dM.keys()):
            dM[magazine[i]] += 1
        else:
            dM[magazine[i]] = 1
    
    dN = {}
    for i in range(len(note)):
        if(note[i] in dN.keys()):
            dN[note[i]] += 1
        else:
            dN[note[i]] = 1

    flag = False
        
    for i in dN.keys():
        if(i in dM.keys()):
            if(dN[i] <= dM[i]):
                continue
            else:
                flag = True
        else:
            flag = True
            
    if(flag == True):
        print("No")
        return 
    else:
        print("Yes")
        return

    # dFinal = dM.items() & dN.items()

    # unmatched_item = set(dict(dFinal).items()) ^ set(dN.items())
    # print(unmatched_item)

    # print(dict(dFinal))
    # print(dN)
    # print(dM)

    # if(dict(dFinal) == dN):
    #     print("Yes")
    # else:
    #     print("No")
    return 

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
