##
##
##class Node:
##    def __init__(self,data):
##        self.data=data
##        self.next=None
##def printLL(head):
##    while head is not None:
##        print(head.data,end=" ")
##        head=head.next
##    print()
##    return
##def takeInput():
##    inputList=[int(ele) for ele in input().split()]
##    head=None
##    tail=None
##    for currData in inputList:
##        if currData==-1:
##            break
##        newNode=Node(currData)
##        if head is None:
##            head=newNode
##            tail=newNode
##        else:
##            tail.next=newNode
##            tail=newNode
##    return head
##def reverse2(head):
##    if head is None or head.next is None:
##        return head,head
##    smallHead,smallTail=reverse2(head.next)
##    smallTail.next=head
##    head.next=None
##    return smallHead,head
##def rev(head, k):
##        if k == 1:
##            return head
##        last = rev(head.next, k - 1)
##        head.next.next = head
##        head.next = None
##        return last
##def reverse3(head):
##    if head is None or head.next is None:
##        return head
##    smallHead=reverse3(head.next)
##    tail=head.next
##    tail.next=head
##    head.next=None
##    return smallHead
##def KREVERSE(head, n):
##
##    c = 1
##    curr = head
##    if curr is None:
##        return None
##    while curr and c < n:
##        c += 1
##        curr = curr.next
##    head2 = None
##    if curr is not None:
##        
##        head2 = curr.next
##        curr.next = None
####  printLL(head2)
##    new_head, new_tail = reverse2(head)
##    
##    new_tail.next = KREVERSE(head2, n)
##    
##    return new_head
##    
##        #printLL(new_tail)
##
####    c = 0
####    curr = head
####    prev = head
####    while curr and c < n:
####        prev = curr
####        c += 1
####        curr = curr.next
####    if c == n:
####        head2 = curr
####        prev.next = None
####        
####        new_head, new_tail = reverse2(head)
####        new_tail.next = KREVERSE(head2, n)
####
####        return new_head
####        #printLL(new_tail)
####    if c < n:
####        return reverse2(head)
##
##
##        
####    h1 = head
####    t1 = head
####    count = 1
####    
####    while(t1 is not None):
####        
####        if count != n:
####            t1 = t1.next
####            count += 1
####        else:
####            head2 = t1.next
####            printLL(head2)
####            t1.next = None
####            h1, t1 = reverse2(h1)
####            if head2 is not None:
####                t1.next = KREVERSE(head2, n)
####            #return h1
####        if head2 is not None:
####            t1.next = head2
####        return h1
##
##            
##        
##head=takeInput()
###printLL(head)
##n=int(input())
##head=KREVERSE(head,n)
##printLL(head)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count
# def print_linkedlist_spl(head):
#     if head is None:
#         return
#     # head
#     smalllist=print_linkedlist_spl(head.next)
#     smalllist=head
#     return smalllist
def reverse(head2):
    if head2 is None or head2.next is None:
        return head2
    smallHead=reverse(head2.next)
    tail=head2.next
    tail.next=head2
    head2.next=None
    return smallHead
def check_palindrome(head):
    l=length(head)
    mid=l + 1//2
    print(mid)
    curr=head
    count=0
    while count<mid:
        curr=curr.next
        count+=1
    h2=curr.next    
    curr.next=None
    # print_linkedlist_spl(h2)
    # while(h2 is not None):
    #     if(head.data!=h2.data): 
    #         return False
    #     head=head.next
    #     h2=h2.next
    # return True   
    head2 = reverse(h2)
    while head is not None and h2 is not None:
        if head.data != h2.data:
            return False
        head = head.next
        h2 = h2.next
    return True

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")








