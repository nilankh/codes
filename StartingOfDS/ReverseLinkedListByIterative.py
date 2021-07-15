class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return
def takeInput():
    inputList=[int(ele)for ele in input().split()]
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
def reverse(head):
    curr=head
    prev=None
    while(curr is not None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
head=takeInput()
l=reverse(head)
printLL(l)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    curr=head
    prev=None
    while(curr is not None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverse(l)
printll(l)
'''













