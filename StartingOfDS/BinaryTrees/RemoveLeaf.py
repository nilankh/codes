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

def removeLeafNodes(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    root.left=removeLeafNodes(root.left)
    root.right=removeLeafNodes(root.right)
    return root



root=treeInput()
printTree(root)
root=removeLeafNodes(root)
printTree(root)
