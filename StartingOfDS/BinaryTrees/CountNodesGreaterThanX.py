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
def countNodesGreaterThanX(root,x):
    if root==None:
        return 0
    count=0
    if root.data>x:
        count+=1
    countLeft=countNodesGreaterThanX(root.left,x)
    countRight=countNodesGreaterThanX(root.left,x)
    return count+countLeft+countRight
def countNodes(root,x):
    if root==None:
        return 0
    result=0
    if root.data>x:
        result+=1
    result+=countNodes(root.left,x)
    result+=countNodes(root.right,x)
    return result
        
root=treeInput()
printTree(root)
x=int(input())
#print(countNodesGreaterThanX(root,x))
print(countNodes(root,x))











