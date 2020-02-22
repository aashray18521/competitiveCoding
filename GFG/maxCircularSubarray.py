def maxCircularSubarray(arr, n):
	res = arr[0]
	for i in range(0, n):
		curr = arr[i]
		for j in range(0, n):
			idx = (i+j) % n
			if(idx != i):
				curr += arr[idx]
			if(curr > res):
				res = curr
	return res

if __name__=="__main__":
	t = int(input())
	while(t):
		t -= 1
		arr = list(map(int, input().split()))
		print(maxCircularSubarray(arr, len(arr)))