# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1

def intersetPoint(head_a,head_b):
    if(head_a == None or head_b == None):
        return -1
    else:
        while(head_a != None):
            head_a.data = -1 * head_a.data
            head_a = head_a.next
        while(head_b.data > 0 and head_b.next != None):
            head_b = head_b.next
        head_b.data =  head_b.data * -1
        return head_b
    return -1