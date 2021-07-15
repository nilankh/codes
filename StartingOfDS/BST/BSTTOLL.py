'''
BST to LL
Send Feedback
Given a BST, convert it into a sorted linked list. Return the head of LL.
Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Output Format :
Linked list elements (separated by space)
Sample Input :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
Sample Output :
2 5 6 7 8 10
'''





import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printLevelWise(root):
    if root==None:
        return
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        curr=q.get()
        print(curr.data,end=":")
        if curr.left!=None:
            print("L",end=":")
            print(curr.left.data,end=",")
            q.put(curr.left)
        else:
            print("L:-1",end="")
        if curr.right!=None:
            print("R",end=":")
            print(curr.right.data,end="")
            q.put(curr.right)
        else:
            print("R:-1",end="")
        print()

def takeLevelWiseInput():
    q=queue.Queue()
    print("Enter root:")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right Child of",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printll(head):
    while(head):
        print(head.data, end = ' - >')
        head = head.next
    print()
def sortedLLFromBST(root):
    if root == None:
        return None
    left = sortedLLFromBST(root.left)
    curr = Node(root.data)
    curr.next = sortedLLFromBST(root.right)
    if left == None:
        return curr
    ptr = left
    while ptr.next != None:
        ptr = ptr.next
    ptr.next = curr
    return left

    
root=takeLevelWiseInput()
ll = sortedLLFromBST(root)
printll(ll)



printLevelWise(root)
