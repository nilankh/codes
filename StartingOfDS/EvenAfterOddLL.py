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
def arranged_LL(head):
    oddH=None
    oddT=None
    evenH=None
    evenT=None
    while head!=None:
        if head.data%2==1:
            if oddH is None:
                oddH=head
                oddT=head
                head=head.next
            else:
                oddT.next=head
                oddT=oddT.next
                head=head.next
        else:
            if evenH is None:
                evenH=head
                evenT=head
                head=head.next
            else:
                evenT.next=head
                evenT=evenT.next
                head=head.next
            #head=head.next

    if evenT!=None:
        evenT.next=None
    if oddH==None:
        return evenH
    else:
        oddT.next=evenH
        return oddH
  
head=takeInput()
#printLL(head)
k=arranged_LL(head)
printLL(k)

