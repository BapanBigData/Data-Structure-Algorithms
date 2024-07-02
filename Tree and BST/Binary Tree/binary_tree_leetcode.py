from collections import deque

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

########################################################################################################################
## **100. Same Tree**
## Given the roots of two binary trees p and q, write a function to check if they are the same or not.
## Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    ## base cases
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    lt = isSameTree(p.left, q.left)
    rt = isSameTree(p.right, q.right)
    
    return lt and rt


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.left = TreeNode(5)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.right.left = TreeNode(5)

print(isSameTree(p, q))
#########################################################################################################################
## **101. Symmetric Tree**
## Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
def isSymmetric(root: TreeNode) -> bool:
    
    def solver(left, right):
        ## base cases
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        return left.val == right.val and solver(left.left, right.right) and solver(left.right, right.left)
    
    return solver(root.left, root.right)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)

print(isSymmetric(p))
##########################################################################################################################
## **102. Binary Tree Level Order Traversal**
def levelOrder(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    
    queue = deque()
    queue.append(root)
    
    res = []
    
    while queue:
        cnt = len(queue)
        level = []
        
        for _ in range(cnt):
            curr = queue.popleft()
            level.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        
        res.append(level)
    
    return res
#######################################################################################################################
## **103. Binary Tree Zigzag Level Order Traversal**

def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    
    queue = deque()
    queue.append(root)
    
    stack = []
    res = []
    rev = False
    
    while queue:
        cnt = len(queue)
        rev_level = []
        level = []
        
        for _ in range(cnt):
            curr = queue.popleft()
            
            if rev:
                stack.append(curr.val)
            else:
                level.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        
        if rev:
            while stack:
                rev_level.append(stack.pop())
            res.append(rev_level)
        else:
            res.append(level)
        
        rev = not rev
    
    return res
#######################################################################################################################
## **105. Construct Binary Tree from Preorder and Inorder Traversal**

def constructTreeFromPreorderInorder(inOrder: list[int], preOrder: list[int]) -> TreeNode:
    ## initialize the preorder index
    pre_index = [0]
    
    mp = {}
    for i in range(len(inOrder)):
        mp[inOrder[i]] = i 
    
    def solver(insi, inei):
        if insi > inei:
            return None
        
        root = TreeNode(preOrder[pre_index[0]])
        pre_index[0] += 1
        
        if insi == inei:
            return root
        
        i = mp[root.val]
        
        root.left = solver(insi, i-1)
        root.right = solver(i+1, inei)
        
        return root
    
    n = len(inOrder)
    
    return solver(0, n-1)

# inorder = [9, 3, 15, 20, 7]; preorder = [3, 9, 20, 15, 7]
# root = constructTreeFromPreorderInorder(inOrder=inorder, preOrder=preorder)

# inOrderTraversal(root)
# print()
# preOrderTraversal(root)

############################################################################################
## **105. Construct Binary Tree from Postorder and Inorder Traversal**

def constructTreeFromPostorderInorder(inOrder: list[int], postOrder: list[int]) -> TreeNode:
    n = len(inOrder)
    
    ## initializing a post index
    post_indx = [n-1]
    
    mp = {}
    for i in range(len(inOrder)):
        mp[inOrder[i]] = i 
    
    def solver(insi, inei):
        if insi > inei:
            return None
        
        root = TreeNode(postOrder[post_indx[0]])
        post_indx[0] -= 1
        
        if insi == inei:
            return root
        
        i = mp[root.val]
        
        root.right = solver(i+1, inei)
        root.left = solver(insi, i-1)
        
        return root
    
    return solver(0, n-1)


inorder = [9, 3, 15, 20, 7]; postorder = [9, 15, 7, 20, 3]
root = constructTreeFromPostorderInorder(inOrder=inorder, postOrder=postorder)

inOrderTraversal(root)
print()
postOrderTraversal(root)