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

def height(root):
    if root==None:
        return 0
    leftHeight=height(root.left)
    rightHeight=height(root.right)
    return 1 +max(leftHeight,rightHeight)

def diameter(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)

    ld=diameter(root.left)
    rd=diameter(root.right)

    return max(lh+rh+1,ld,rd)



root=treeInput()
printTree(root)
print(height(root))
print(diameter(root))







