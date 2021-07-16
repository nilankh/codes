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
        print(curr.data,end=':')
        if curr.left!=None:
            print("L",end=":")
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
def buildTreeFromPreIn(preorder, inorder):
    '''
inorder -> left root right
preorder -> root left right
step1: find the root
step2: Find inorder of both left and right subtree
step3: Find preOrder of both left and right subtree
step4: Use recursion to build left & right subtree
step5: Connect root with both
    '''
    
    if len(preorder) == 0:
        return None
    #find the root
    rootData = preorder[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None
    #Find inorder of both left and right subtree
    leftInorder = inorder[0:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1 :]

    lenLeftSubtree = len(leftInorder)

    #Find preOrder of both left and right subtree
    leftPreorder = preorder[1:lenLeftSubtree + 1:]
    rightPreorder = preorder[lenLeftSubtree + 1:]

    #Use recursion to build left & right subtree
    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder, rightInorder)

    #Connect root with both
    root.left = leftChild
    root.right = rightChild
    return root
    
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreeFromPreIn(preorder, inorder)
printLevelWise(root)


































