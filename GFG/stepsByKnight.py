# https://practice.geeksforgeeks.org/problems/steps-by-knight/0

class cell:
    
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
        
def isInside(x, y, n):
    if(x >= 1 and x <= n and y >= 1 and y <= n):
        return True
    return False

def stepCount(n, start, end):
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]
    
    q = []
    visited = [[False for i in range(n+1)] for j in range(n+1)]
    
    temp = cell(start[0], start[1], 0)
    q.append(temp)
    visited[start[0]][start[1]] = True
    
    while(len(q) > 0):
        t = q[0]
        q.pop(0)
        
        if(t.x == end[0] and t.y == end[1]):
            return t.dist
        
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            
            if(isInside(x, y, n) and not visited[x][y]):
                q.append(cell(x, y, t.dist + 1))
                visited[x][y] = True
    
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))
        # stepCount(n, start, end)
        print(stepCount(n, start, end))