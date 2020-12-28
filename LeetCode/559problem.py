"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if(root == None):
            return 0
        res = 0
        for child in root.children:
            t = self.maxDepth(child)
            res = max(res, t)
        return res + 1