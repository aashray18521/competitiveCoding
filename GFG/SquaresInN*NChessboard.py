# https://practice.geeksforgeeks.org/problems/squares-in-nn-chessboard/0

if __name__=="__main__":
    t = int(input())
    while(t):
        t -= 1
        n = int(input())
        val = n*(n+1)*(2*n+1)/6
        print(int(val))