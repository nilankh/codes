class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def isNodePresent(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    res1=isNodePresent(root.left,x)
    res2=isNodePresent(root.right,x)
    return res1 or res2

root=treeInput()
printTree(root)
x=int(input())
if isNodePresent(root,x):
    print("true")
else:
    print("false")





