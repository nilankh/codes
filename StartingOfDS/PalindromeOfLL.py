class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head'''
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
    
def check_palindrome(head):
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    head1=head
    head2=slow.next
    slow.next=None
    head2=reverse(head2)
    
    while head1 is not None and head2 is not None:
        if head1.data!=head2.data:
            return False
        head1=head1.next
        head2=head2.next
    return True

def reverse(head2):
    if head2 is None or head2.next is None:
        return head2
    smallHead=reverse(head2.next)
    tail=head2.next
    tail.next=head2
    head2.next=None
    return smallHead

from sys import setrecursionlimit
setrecursionlimit(10000)
#arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
#l = ll(arr[:-1])
head=takeInput()
ans = check_palindrome(head)
if ans:
    print("true")
else:
    print("false")
