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
def mergeTwoSortedLL(head1,head2):
    final_head=None
    final_tail=None

    if(head1.data<=head2.data):
        final_head=head1
        final_tail=head1
        head1=head1.next
    else:
        final_head=head2
        final_tail=head2
        head2=head2.next
    while(head1!=None and head2!=None):
        if(head1.data<=head2.data):
            final_tail.next=head1
            final_tail=final_tail.next
            head1=head1.next
        else:
            final_tail.next=head2
            final_tail=final_tail.next
            head2=head2.next
            
    if(head1 is not None):
        final_tail.next=head1
    if(head2 is not None):
        final_tail.next=head2
    return final_head
def mergeSort(head):
    if head.next is None:
        return head
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    #head1=head
    head2=slow.next
    slow.next=None

    head=mergeSort(head)
    head2=mergeSort(head2)
    return mergeTwoSortedLL(head,head2)
l=takeInput()
#printLL(head)
l=mergeSort(l)
printLL(l)













    
