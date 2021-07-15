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

def takeInput():
    rootData=int(input())
    if rootData == -1:
        return None

    root=BinaryTreeNode(rootData)
    leftTree=takeInput()
    rightTree=takeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def sumOfAllNodes(root):
    if root==None:
        return 0
    return root.data+sumOfAllNodes(root.left)+sumOfAllNodes(root.right)

root=takeInput()
printTree(root)
print(sumOfAllNodes(root))
