#  Mirror Tree 
# https://practice.geeksforgeeks.org/problems/mirror-tree/1
# For some wierd reason, the code with same logic was working fine in c++
# but not in Python
# I tried with queue logic as well

def mirror(root):
    if(root == None):
        return
    else:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left
    return