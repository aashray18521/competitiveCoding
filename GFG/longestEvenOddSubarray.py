def longestEvenOddSubarray(arr, n):
    res = 1
    curr = 1
    for i in range(1, n):
        if((arr[i-1]%2 == 0 and arr[i]%2 != 0) or (arr[i-1]%2 != 0 and arr[i]%2 == 0)):
            curr += 1
            res = max(res, curr)
        else:
            curr = 1
    return res

if __name__=="__main__":
    t = int(input())
    while(t):
        t -= 1
        arr = list(map(int, input().split()))
        print(longestEvenOddSubarray(arr, len(arr)))