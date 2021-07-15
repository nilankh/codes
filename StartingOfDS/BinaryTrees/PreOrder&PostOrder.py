class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preOrder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)
    
def postOrder(root):
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
    
def takeInput():
    rootData=int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree=takeInput()
    rightTree=takeInput()
    root.left=leftTree
    root.right=rightTree
    return root

root=takeInput()
preOrder(root)
#postOrder(root)
inOrder(root)
#1 2 4 5 3 6 7 4 2 5 1 6 3 7 

