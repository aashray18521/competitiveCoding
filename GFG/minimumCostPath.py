# https://practice.geeksforgeeks.org/problems/minimum-cost-path/0

def minCost(arr, n): 
    
    tempCost = [[0 for i in range(n)] for j in range(n)]
    
    tempCost[0][0] = arr[0][0]
    
    for i in range(1, n):
        tempCost[0][i] = tempCost[0][i-1] + arr[0][i]
    
    for i in range(1, n):
        tempCost[i][0] = tempCost[i-1][0] + arr[i][0]
        
    for i in range(1, n):
        for j in range(1, n):
            tempCost[i][j] = min(tempCost[i-1][j], tempCost[i][j-1]) + arr[i][j]
    
    return tempCost[n-1][n-1]
    
if __name__=="__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        matrix = [[arr[j+n*i] for j in range(n)] for i in range(n)]
        
        print(minCost(matrix, n))