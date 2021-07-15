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
'''
def eliminate_duplicates(head):
    t1=head
    if t1 is None:
        return head
    else:
        t2=head.next
    while t2!=None:
        if t1.data==t2.data:
            t1.next=t2.next
            t2=t2.next
        else:
            t1=t2
            t2=t2.next
    return head'''
#2nd method of eliminating duplicates
def eliminate_duplicates(head):
    temp=head
    if temp is None:
        return head
    while temp.next is not None:
        if temp.data==temp.next.data:
            new=temp.next.next
            temp.next=None
            temp.next=new
        else:
            temp=temp.next
    return head
head=takeInput()
printLL(head)
l=eliminate_duplicates(head)
printLL(l)



