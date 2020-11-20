class Solution():
  def solve(self, num):
    temp = str(num)
    l = len(temp)
    res = float('-inf')
    for i in range(l):
      curr = temp[:i] + "5" + temp[i:]
      if(i == 0 and temp[i] == "-"):
        continue
      res = max(res, int(curr))
    return res
    
obj = Solution()
print(obj.solve(846))
