# https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1

def deleteNode(curr_node):
    #code here
    if(curr_node.next == None or curr_node == None):
        return
    else:
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next