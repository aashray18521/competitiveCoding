# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/

def lenLinkedList(head):
    count = 0
    if(head == None):
        return 0
    elif(head.next == None and head.data != None):
        return 1
    else:
        while(head.next != None):
            count += 1
            head = head.next
        return count+1

def linkedListToArray(head):
    arr = []
    if(head == None):
        return arr
    elif(head.next == None):
        arr.append(head)
        return arr
    else:
        while(head != None):
            arr.append(head.data)
            head = head.next
        return arr

def isPalindrome(head):
    flag = True
    arr = linkedListToArray(head)
    lenLinkedLst = len(arr)
    for i in range(0, lenLinkedLst):
        if(arr[i] != arr[lenLinkedLst-i-1]):
            flag = False
            break
        else:
            continue
    if(flag == True):
        return 1
    else:
        return 0

