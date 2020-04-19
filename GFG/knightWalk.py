# https://practice.geeksforgeeks.org/problems/knight-walk/0
class cell:
    
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
        
def isInside(x, y, n, m):
    if(x >= 1 and x <= n and y >= 1 and y <= m):
        return True
    return False

def kinghtWalk(n, m, s1, s2, d1, d2):
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]
    
    q = []
    visited = [[False for i in range(m+1)] for j in range(n+1)]
    
    temp = cell(s1, s2, 0)
    q.append(temp)
    visited[s1][s2] = True
    
    while(len(q) > 0):
        t = q[0]
        q.pop(0)
        
        if(t.x == d1 and t.y == d2):
            return t.dist
        
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            
            if(isInside(x, y, n, m) and not visited[x][y]):
                q.append(cell(x, y, t.dist + 1))
                visited[x][y] = True
    return -1
    
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().split()))
        n, m = temp[0], temp[1]
        temp = []
        temp = list(map(int, input().split()))
        s1, s2, d1, d2 = temp[0], temp[1], temp[2], temp[3]
        print(kinghtWalk(n, m, s1, s2, d1, d2))
