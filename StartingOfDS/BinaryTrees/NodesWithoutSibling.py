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

def nodesWithoutSibling(root):
    if root==None:
        return

    if root.left==None and root.right!=None:
        #right node has no sibling.Print right node and call Recursion
        print(root.right.data)
        nodesWithoutSibling(root.right)
        return

    if root.left!=None and root.right==None:
        #left node has no sibling.print left node and call recursion
        print(root.left.data)
        nodesWithoutSibling(root.left)
        return
    nodesWithoutSibling(root.right)
    nodesWithoutSibling(root.left)
root=treeInput()
printTree(root)
nodesWithoutSibling(root)








