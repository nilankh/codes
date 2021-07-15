import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printLevelAtNewLine(root):
    if root==None:
        return
    q1=queue.Queue()
    #print(q1)
    q2=queue.Queue()
    #print(q2)
    q1.put(root)
    while not q1.empty():
        while not q1.empty():
            curr=q1.get()
            #print(curr)
            print(curr.data,end=" ")
            if curr.left!=None:
                q2.put(curr.left)
                #print("ye kaam kia")
                #print("pehl if",q2.get)
            if curr.right!=None:
                q2.put(curr.right)
                #print("right wala kaam kia")
                #print("q2",q2.get)
        q1,q2=q2,q1
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

root=takeLevelWiseInput()
printLevelAtNewLine(root)

        
