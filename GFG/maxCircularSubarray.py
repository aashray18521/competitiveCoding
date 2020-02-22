def maxCircularSubarray(arr, n):
	res = arr[0]
	for i in range(0, n):
		curr = arr[i]
		for j in range(1, n):
			idx = (i+j) % n
			curr += arr[idx]
			res = max(curr, res)
	return res

def maxArrSubsequence(arr):
    res = arr[0]
    curr = arr[0]
    for i in range(1, len(arr)):
        curr = max(arr[i], curr+arr[i])
        res = max(curr, res)
    return res

def minSumSubarray(arr, n):
    res = arr[0]
    curr = arr[0]
    for i in range(1, n):
        curr = min(arr[i], curr+arr[i])
        res = min(res, curr)
    return res
    
def arrSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def maxSumCircularSubarray(arr): #OPTIMIZED
    val1 = maxArrSubsequence(arr)
    val2 = arrSum(arr) - minSumSubarray(arr, len(arr))
    return max(val1, val2)

if __name__=="__main__":
	t = int(input())
	while(t):
		t -= 1
		arr = list(map(int, input().split()))
		print(maxCircularSubarray(arr, len(arr)))