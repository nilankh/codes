import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

INT_MIN = -2147483648
INT_MAX = 2147483647

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

def minMax(root):
    if root==None:
        return 2147483647,-2147483648

    leftmin,leftmax=minMax(root.left)
    rightmin,rightmax=minMax(root.right)
    minimum=min(leftmin,rightmin,root.data)
    maximum=max(leftmax,rightmax,root.data)
    
    return minimum,maximum

root=takeLevelWiseInput()
minimum, maximum = minMax(root)
print(maximum, minimum)
