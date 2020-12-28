# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = TreeNode()
        if(t1 == None and t2):
            t3 = t2
        elif(t2 == None and t1):
            t3 = t1
        elif(t1 and t2):
            t3.val = t1.val + t2.val
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        else:
            t3 = None
        return t3