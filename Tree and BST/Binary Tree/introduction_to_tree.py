from collections import deque
import math

class TreeNode:
    
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(root: TreeNode):
    ## base case
    if root is None:
        return
    
    inOrderTraversal(root.left)
    print(root.val, end=' ')
    inOrderTraversal(root.right)
    
    return


def preOrderTraversal(root: TreeNode):
    ## base case
    if root is None:
        return
    
    print(root.val, end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    
    return


def postOrderTraversal(root: TreeNode):
    ## base case
    if root is None:
        return
    
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.val, end=' ')
    
    return


def heightOfTree(root: TreeNode):
    ## base cases
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    leftTree = heightOfTree(root.left)
    rightTree = heightOfTree(root.right)
    
    return max(leftTree, rightTree) + 1


def printAtDistK(root: TreeNode, k: int):
    ## base case
    if root is None:
        return
    
    if k == 0:
        print(root.val, end=' ')
        return
    
    printAtDistK(root.left, k-1)
    printAtDistK(root.right, k-1)
    
    return

## BFS
def levelOrderTraversal(root: TreeNode):
    if root is None:
        return
    
    q = deque()
    q.append(root)
    
    while q:
        curr = q.popleft()
        print(curr.val, end=' ')
        
        if curr.left:
            q.append(curr.left)
        
        if curr.right:
            q.append(curr.right)
    
    return


def sizeOfTree(root: TreeNode):
    ## base case
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    leftSize = sizeOfTree(root.left)
    rightSize = sizeOfTree(root.right)
    
    return leftSize + rightSize + 1


def getMaxTree(root: TreeNode):
    ## base case
    if root is None:
        return -math.inf
    
    if root.left is None and root.right is None:
        return root.val
    
    leftTree = getMaxTree(root.left)
    rightTree = getMaxTree(root.right)
    
    return max(leftTree, rightTree, root.val)


## code to build the tree
root = TreeNode(30)
root.left = TreeNode(40)
root.right = TreeNode(50)
root.left.left = TreeNode(100)
root.right.left = TreeNode(70)
root.right.right = TreeNode(80)

root1 = TreeNode(10)
root1.left = TreeNode(8)
root1.right = TreeNode(30)
root1.right.left = TreeNode(40)
root1.right.right = TreeNode(50)
root1.right.right.left = TreeNode(70)

root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(8)
root2.left.right = TreeNode(7)
root2.left.right.left = TreeNode(9)
root2.left.right.right = TreeNode(15)
root2.right.right = TreeNode(6)

# print(sizeOfTree(root))
# print(sizeOfTree(root1))
# print(sizeOfTree(root2))

print(getMaxTree(root))
print(getMaxTree(root1))
print(getMaxTree(root2))

# levelOrderTraversal(root1)
# inOrderTraversal(root)
# print()
# preOrderTraversal(root)
# print()
# postOrderTraversal(root)

# print(heightOfTree(root1))
# printAtDistK(root, k=2)