class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) + " -> ",end = "")
        head = head.next
    print("None")
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
def swap_nodes(head, i, j):
    curr = head
    prev = previ = curri = prevj = currj = None
    count = 0
    while(curr != None):
        if count == i:
            previ = prev
            curri = curr
        elif count == j:
            prevj = prev
            currj = curr
        prev = curr
        curr = curr.next
        count += 1
    if(curri == None or currj == None):
        return
    if previ == None:
        head = currj
        #printLL(head)
    else:
        previ.next = currj
        #printLL(head)
    if prevj == None:
        head = curri
    else:
        prevj.next = curri
##        printLL(prevj)
    curr = curri.next
    #printLL(curr)
    curri.next = currj.next
    #printLL(curri)
    currj.next = curr
    #printLL(currj)
    return head





head = takeInput()
i, j =[int(x) for x in input().split()]
#printLL(head)
l = swap_nodes(head, i, j)
printLL(l)








