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

def swapNodes(head, i, j) :
    if( i == j):
        return head
    if(i > j):
        i, j = j, i
        
    p1 = None
    p2 = None
    temp1 = head
    temp2 = head
    if(i == 0):
        for i in range(1, j + 1):
            p2 = temp2
            temp2 = temp2.next
        if j ==1:
            a = temp2.next
            temp2.next = temp1
            temp1.next = a
            return temp2
        
        a = temp1.next
        temp1.next = temp2.next
        p2.next = temp1
        temp2.next = a
        return temp2
    
    for i in range(1, i + 1):
        p1 = temp1
        temp1 = temp1.next
    for i in range(1, j + 1):
        p2 = temp2
        temp2 = temp2.next
    
    
    p1.next = temp2
    p2.next = temp1
    a = temp1.next
    temp1.next = temp2.next
    temp2.next = a
    return head



head = takeInput()
i, j =[int(x) for x in input().split()]
#printLL(head)
l = swap_nodes(head, i, j)
printLL(l)








