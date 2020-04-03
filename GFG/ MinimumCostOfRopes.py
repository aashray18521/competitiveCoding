# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0

import heapq

def fn():
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    heapq.heapify(a)
    sumi = 0
    while(True):
        if len(a) == 1:
            break
        tmp1 = heapq.heappop(a)
        tmp2 = heapq.heappop(a)
        heapq.heappush(a,tmp1+tmp2)
        sumi += tmp1+tmp2
        #print(a)
    print(sumi)

for _ in range(int(input().strip())):
    fn()