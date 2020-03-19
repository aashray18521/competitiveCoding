# https://practice.geeksforgeeks.org/problems/reverse-the-string/0

if __name__ == "__main__":
    t = int(input())
    while(t):
        t -= 1
        s = input()
        l = len(s)
        beg = 0
        end = l-1
        ns = []
        while(end >= beg):
            ns.append(s[end])
            end -= 1
        s = "".join(ns)
        print(s)