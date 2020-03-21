# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0

def missingAndRepeating(arr, n):
    for i in range(n):
        if(arr[abs(arr[i]) - 1]) > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print(abs(arr[i]), end=" ")
    for i in range(n):
        if(arr[i]) > 0:
            print(i+1)
    return

if __name__=="__main__":
    testcases= int(input())
    arr=[]
    temp=[0]
    for i in range(testcases):
        n=int(input()) 
        temp=input().split()
        for i in range(len(temp)):
            temp[i]=int(temp[i])
            arr.append(temp)
        missingAndRepeating(arr[-1], n)