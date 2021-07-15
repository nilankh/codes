

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head=head.next
    print()
    return
def takeInput():
    inputList=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def reverse2(head):
    if head is None or head.next is None:
        return head,head
    smallHead,smallTail=reverse2(head.next)
    smallTail.next=head
    head.next=None
    return smallHead,head
#one method as in hint
def KREVERSE(head, n):
    c = 1
    curr = head
    if curr is None:
        return None
    while curr and c < n:
        c += 1
        curr = curr.next
    head2 = None
    if curr is not None:
        head2 = curr.next
        curr.next = None
    new_head, new_tail = reverse2(head)
    new_tail.next = KREVERSE(head2, n)

    return new_head

#second method   
##def KREVERSE(head,n):
##    curr=head
##    next=None
##    prev=None
##    count=0
##    while(curr is not None and count<n):
##        next=curr.next
##        curr.next=prev
##        prev=curr
##        curr=next
##        count+=1
##    if next is not None:
##        head.next=KREVERSE(next,n)
##    return prev
head=takeInput()
#printLL(head)
n=int(input())
head=KREVERSE(head,n)
printLL(head)


















        
