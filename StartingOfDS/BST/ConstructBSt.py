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
            print("L:-1,",end="")
        if curr.right!=None:
            print("R",end=":")
            print(curr.right.data,end="")
            q.put(curr.right)
        else:
            print("R:-1",end="")
        print()

def takeLevelWiseInput():
    q=queue.Queue()
    print("enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right child of ",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)
def constructBST(lst):
    start=0
    end=len(lst)-1
    while start<=end:
        mid=(start+end)//2
        rootData=lst[mid]
        root=BinaryTreeNode(rootData)
        leftSide=constructBST(lst[:mid])
        rightSide=constructBST(lst[mid+1:])
        root.left=leftSide
        root.right=rightSide
        return root

#solutionofcn
def constructBst(lst):
    n=len(lst)
    if lst==None or n<=0:
        return None
    rootIndex=(n-1)//2
    root=BinaryTreeNode(lst[rootIndex])
    root.left=constructBst(lst[:rootIndex])
    root.right=constructBst(lst[rootIndex+1:])
    return root
#root=takeLevelWiseInput()
#printLevelWise(root)
n=int(input())
lst=[int(f) for f in input().split()]
#root=constructBST(lst)
#printLevelWise(root)
#preOrder(root)
root=constructBst(lst)
preOrder(root)




