class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def linearSearchRecursive(head,n,index=0):
    if head is None:
        return -1
    if head.data==n:
        return index
    return linearSearchRecursive(head.next,n,index+1)'''
def linearSearchRecursive(head,n):
    if head==None:
        return -1
    if(head.data==n):
        return 0
    result=linearSearchRecursive(head.next,n)
    if result==-1:
        return -1
    return 1+result
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
'''   
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
'''
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
#arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
#l = ll(arr[:-1])
head=takeInput()
data=int(input())
index = linearSearchRecursive(head, data)
print(index)
