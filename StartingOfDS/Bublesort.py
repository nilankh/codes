class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(str(head.data) +"->",end="")
        head=head.next
    print("None")
    return
def takeInput():
    inputList=[int(ele) for ele in input().split()]
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

def lengthRecursive(head):
    if head is None:
        return 0
    else:
        return 1+lengthRecursive(head.next)
def bubbleSortLL(head):
    if head == None or head.next == None:
        return head
    
    for i in range(0, lengthRecursive(head)):
        curr = head
        prev = None
        Next = curr.next
        while curr.next != None:
            if curr.data > curr.next.data:
                if prev is None:
                    curr.next = Next.next
                    Next.next = curr
                    head = Next
                else:
                    prev.next = curr.next
                    curr.next = Next.next
                    Next.next = curr
                prev = Next
                Next = curr.next
                

            else:
                prev = curr
                curr = curr.next
                Next = curr.next
    return head



    
head = takeInput()
k = bubbleSortLL(head)
printLL(k)



























