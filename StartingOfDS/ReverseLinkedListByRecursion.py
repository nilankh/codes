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



def reverse1(head):

    
    if head is None or head.next is None:
        return head
    smallHead = reverse1(head.next)
    curr = smallHead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallHead
        
    

def reverse(head):
    if head is None:
        return
    reverse(head.next)
    print(head.data,end=" ")
    
#another way by recursion
def reverse2(head):
    if head is None or head.next is None:
        return head,head
    smallHead,smallTail=reverse2(head.next)
    smallTail.next=head
    head.next=None
    return smallHead,head


#another way again
def reverse3(head):
    if head is None or head.next is None:
        return head
    smallHead=reverse3(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallHead

head=takeInput()
printLL(head)
#head = reverse1(head)
#reverse(head)
#l=reverse2(head)
head,tail=reverse2(head)
printLL(head)
#l=reverse3(head)
#printLL(l)



















