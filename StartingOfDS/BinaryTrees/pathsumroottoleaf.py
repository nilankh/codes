import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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


def pathSumRootToLeaf(root,k,lst):
    if root==None:
        return
    if root.left==None and root.right==None and root.data==k:
        print(*lst,root.data)
        return
    lst.append(root.data)
    pathSumRootToLeaf(root.left,k-root.data,lst)
    pathSumRootToLeaf(root.right,k-root.data,lst)
    lst.pop()
    return


    
root=takeLevelWiseInput()
k=int(input())
pathSumRootToLeaf(root,k,[])




















