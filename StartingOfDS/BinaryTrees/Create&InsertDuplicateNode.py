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
            print("L",end="")
            print(curr.left.data,end=",")
            q.put(curr.left)
        else:
            print("L:-1,",end="")
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
        print("ENTER LEFT CHILD OF ",current_node.data)
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

def insertDuplicateNode(root):
    if root==None:
        return
##    q=queue.Queue()
##    q.put(root)
    duplicate=BinaryTreeNode(root.data)
    
    leftRoot=insertDuplicateNode(root.left)
    rightRoot=insertDuplicateNode(root.right)
    root.left=duplicate
    duplicate.left=leftRoot
    root.right=rightRoot
    return root
def def insertDuplicateNode2(root):
    if root == None:
        return
    newNode = BinaryTreeNode(root.data)
    rootLeft = root.left

    root.left = newNode
    newNode.left = rootLeft

    insertDuplicateNode2(root.left)
    insertDuplicateNode2(root.right)
root=takeLevelWiseInput()
printLevelWise(root)
insertDuplicateNode(root)
printLevelWise(root)










        
