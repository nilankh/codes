'''
LCA of BST
Send Feedback
Given a binary search tree and two nodes, find LCA(Lowest Common Ancestor) of the given two nodes in the BST. Read about LCA if you are having doubts about the definition.
If out of 2 nodes only one node is present, return that node.
If both are not present, return -1.
Input format :
Line 1 :  Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Two integers, Node 1 and Node 2 (separated by space)
Output Format :
LCA
Constraints :
1 <= N <= 1000
Sample Input 1:
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
2 10
Sample Output 1:
8
Sample Input 2:
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
2 6
Sample Output 2:
5
'''



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
            print("L",end=":")
            print(curr.left.data,end=",")
            q.put(curr.left)
        else:
            print("L:-1",end="")
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
        print("ENTER LEFT CHILD OF",current_node.data)
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
''' it needs modification for somecases
def lcaOfBst(root, val1, val2):
    if root == None:
        return
    if root.data > max(val1, val2):
        return lcaOfBst(root.left, val1, val2)
    elif root.data < min(val1, val2):
        return lcaOfBst(root.right, val1, val2)
    else:
        return root.data
'''
def lcaOfBstHelper(root, a, b):
    if root == None:
        return None
    if root.data == a or root.data == b:
        return root
    if root.data < a and root.data < b :
        return lcaOfBstHelper(root.right, a, b)
    elif root.data > a and root.data > b:
        return lcaOfBstHelper(root.left, a, b)
    else:
        left_lca = lcaOfBstHelper(root.left, a, b)
        right_lca = lcaOfBstHelper(root.right, a, b)
        if(left_lca != None and right_lca != None):
            return root
        elif left_lca != None:
            return left_lca
        else:
            return right_lca
def lcaOfBst(root, a, b):
    node = lcaOfBstHelper(root, a, b)
    if(node != None):
        return node.data
    else:
        return -1
    
root=takeLevelWiseInput()
a,b = (int(i) for i in input().strip().split())
print(lcaOfBst(root, a, b))


