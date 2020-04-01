# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

'''
Structure of node
class Node:
    data=0
    next=None
'''
##Complete this function

def lenLoop(head):
    if(detectloop(head) == 0):
        return 0
    else:
        single = head
        double = head.next
        while(single != double):
            double = double.next.next
            single = single.next
        lenloop = 1
        while(double.next != single):
            double = double.next
            lenloop += 1
        return lenloop
    return -1
    
def removeTheLoop(head):
    ##Your code here
    if(detectloop(head) == 0):
        return
    else:
        loop = lenLoop(head)
        lenList = length(head, True)
        val = lenList - loop
        while(val):
            head = head.next
            val -= 1
        loop -= 1
        while(loop):
            head = head.next
            loop -= 1
        head.next = None
    return




#{ 
#  Driver Code Starts
class Node:
    data=0
    next=None
    
    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp
    
def insert(head,data):
    if(head==None):
        head=newNode(data)
    else:
        head.next=insert(head.next,data)
    return head

def makeLoop(head,x):
    if (x==0):
        return
    curr=head
    last=head
    counter=0
    while(counter<x):
        curr=curr.next
        counter+=1
    while(last.next!=None):
        last=last.next
    last.next=curr
            

def detectloop(head):
    hare=head.next
    tortoise=head
    while(hare!=tortoise and hare!=None and tortoise!=None):
        hare=hare.next
        tortoise=tortoise.next
        if(hare!=None and hare.next!=None):
            hare=hare.next
        if(hare==tortoise):
            return 1
    return 0
    
def length(head, hasloop):
    len=0
    if(hasloop==False):
        temp=head
        while(temp!=None):
            len+=1
            temp=temp.next
        return len
    else:
        hare=head.next
        tortoise=head
        while(hare!=tortoise):
            hare=hare.next
            tortoise=tortoise.next
            hare=hare.next
            if(hare==tortoise):
                break
        looplen=0
        while(hare.next!=tortoise):
            hare=hare.next
            looplen+=1
        looplen+=1
        begin=head
        startlen=0
        tortoise=tortoise.next
        while(begin!=tortoise):
            begin=begin.next
            tortoise=tortoise.next
            startlen+=1
        return looplen+startlen
        

def main():
    testcases=int(input())
    
    while(testcases>0):
        head=Node()
        head=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        x=int(input())
        
        for i in arr:
            head=insert(head,i)
        makeLoop(head,x)
        lengthll=0
        if(detectloop(head)==1):
            lengthll=length(head,True)
        else:
            lengthll=length(head,False)
        removeTheLoop(head)
        
        if(detectloop(head)==0 and lengthll==length(head,False)):
            print("1")
        else:
            print("0")
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends