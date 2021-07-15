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

def isBST2(root):
    if root==None:
        return 100000,-100000,True
    leftMin,leftMax,isLeftBST=isBST2(root.left)
    rightMin,rightMax,isRightBST=isBST2(root.right)
    minimum=min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)
    isTreeBST=True
    if root.data<=leftMax or root.data>rightMin:
        isTreeBST=False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST=False
    return minimum,maximum,isTreeBST

root=takeLevelWiseInput()
printLevelWise(root)
print(isBST2(root))





