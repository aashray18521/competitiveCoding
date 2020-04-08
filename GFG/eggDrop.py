# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0

INT_MAX = 999

def eggDrop(n, k): 

    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    for i in range(1, n+1): 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
  
    for j in range(1, k+1): 
        eggFloor[1][j] = j 
  
    for i in range(2, n+1): 
        for j in range(2, k+1): 
            eggFloor[i][j] = INT_MAX 
            for x in range(1, j+1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res 
  
    return eggFloor[n][k] 

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        inps = list(map(int, input().split()))
        n, k = inps[0], inps[1]
        print(eggDrop(n, k))