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
    print("ENTER ROOT:")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("ENTER LEFT CHILD OF",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("ENTER RIGHT CHILD OF",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root

def minTree(root):
    if root==None:
        return 100000
    leftMin=minTree(root.left)
    rightMin=minTree(root.right)

    return min(leftMin,rightMin,root.data)

def maxTree(root):
    if root==None:
        return -100000
    leftMax=maxTree(root.left)
    rightMax=maxTree(root.right)

    return max(leftMax,rightMax,root.data)

def isBST(root):
    if root==None:
        return True
    leftMax=maxTree(root.left)
    rightMin=minTree(root.right)
    if root.data>rightMin or root.data<=leftMax:
        return False
    isLeftBST=isBST(root.left)
    isRightBST=isBST(root.right)

    return isLeftBST and isRightBST

root=takeLevelWiseInput()
printLevelWise(root)
print(isBST(root))







