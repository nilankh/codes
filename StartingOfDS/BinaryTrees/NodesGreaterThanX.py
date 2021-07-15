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
    if rootData == -1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root
def nodesGreaterThanX(root):
    if root is None:
        return 0
    count = 0
    if root.data > x:
        count += 1
    leftC = nodesGreaterThanX(root.left)
    rightC = nodesGreaterThanX(root.right)
    return count + leftC + rightC

root=treeInput()
printTree(root)
x = int(input())
print(nodesGreaterThanX(root))
























        
