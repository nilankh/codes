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

def elementsInRangeK1K2(root,k1,k2):
    if root==None:
        return
    if root.data>k2:
        elementsInRangeK1K2(root.left,k1,k2)
    elif root.data<k1:
        elementsInRangeK1K2(root.right,k1,k2)
    else:
        elementsInRangeK1K2(root.left,k1,k2)
        print(root.data,end=" ")
        elementsInRangeK1K2(root.right,k1,k2)


        
root=takeLevelWiseInput()
printLevelWise(root)
k1,k2=[int(z) for z in input().split()]
elementsInRangeK1K2(root,k1,k2)








