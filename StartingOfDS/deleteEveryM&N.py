class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(head.data , end = " ")
        head = head.next
    return
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def skipMdeleteN(head, m, n):
 
 
    if m==0:
        return None
    if n==0:
        return head
    curr=head
    while(curr):
        for count in range(1,m):
            if curr is None:
                return head
            curr=curr.next
        if curr is None:
            return head
        #delete
        if curr.next==None:
            return head
        t=curr.next.next
        for count in range(1,n):
            if t is None:
                break
            t=t.next
        curr.next=t
        curr=t
    return head  
    
head = takeInput()
m = int(input())
n = int(input())
#printLL(head)
l = skipMdeleteN(head, m, n)
printLL(l)






