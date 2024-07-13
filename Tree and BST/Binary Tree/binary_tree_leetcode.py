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


# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(3)
# p.right.left = TreeNode(5)

# q = TreeNode(1)
# q.left = TreeNode(2)
# q.right = TreeNode(3)
# q.right.left = TreeNode(5)

# print(isSameTree(p, q))
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


# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(2)

# print(isSymmetric(p))
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


# inorder = [9, 3, 15, 20, 7]; postorder = [9, 15, 7, 20, 3]
# root = constructTreeFromPostorderInorder(inOrder=inorder, postOrder=postorder)

# inOrderTraversal(root)
# print()
# postOrderTraversal(root)

#####################################################################################################################
## **112. Path Sum**
## Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up 
## all the values along the path equals targetSum.

def pathSumI(root: TreeNode, targetSum: int) -> bool:
    
    def solver(root, currSum):
        ## base cases
        if root is None:
            return False
        
        currSum += root.val
        
        if root.left is None and root.right is None:
            return currSum == targetSum
        
        left = solver(root.left, currSum)
        right = solver(root.right, currSum)
        
        return left or right
    
    return solver(root, 0)
##--------------------------------------------------------------------------------------------------------------
## **113. Path Sum II**
## Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
## Each path should be returned as a list of the node values, not node references.
def pathSumII(root: TreeNode, targetSum: int) -> list[list[int]]:
    paths = []
    
    def solver(root, currSum, currPath):
        ## base cases
        if root is None:
            return []
        
        currSum += root.val
        currPath = currPath + [root.val]
        
        if root.left is None and root.right is None:
            if currSum == targetSum:
                paths.append(currPath)
                return True
            else:
                ## backtracking
                currPath.pop()
                return False
        
        left = solver(root.left, currSum, currPath)
        right = solver(root.right, currSum, currPath)
        
        return left or right
    
    def solver1(root, currSum, currPath, paths):
        ## base cases
        if root is None:
            return []
        
        currSum += root.val
        currPath = currPath + [root.val]
        
        if not root.left and not root.right:
            if currSum == targetSum:
                paths.append(currPath)
                return paths
        
        solver1(root.left, currSum, currPath, paths)
        solver1(root.right, currSum, currPath, paths)
        
        return paths
    
    solver(root, 0, currPath=[])
    
    return paths, solver1(root, 0, currPath=[], paths=[])

###############################################################################################################
## **437. Path Sum III**
## Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
## Note: The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
def pathSumIII(root: TreeNode, targetSum: int) -> int:
    ## Naive soln works with T.C: O(n^2)
    
    def getCnt(node, currSum):
        if node is None:
            return 0
        
        cnt = 0
        currSum += node.val
        
        if currSum == targetSum:
            cnt += 1
        
        cnt += getCnt(node.left, currSum)
        cnt += getCnt(node.right, currSum)
        
        return cnt 
    
    def dfs(root):
        if root is None:
            return 0
        
        count = getCnt(root, 0)
        count += dfs(root.left)
        count += dfs(root.right)
        
        return count
    
    return dfs(root)
######################################################################################################################
## **124. Binary Tree Maximum Path Sum**
def maxPathSum(root: TreeNode) -> int:
    mx = [-math.inf]
    
    def maxPath(node):
        if node is None:
            return 0
        
        left_sum = max(0, maxPath(node.left))      ## Do not consider negative path sum!!!
        right_sum = max(0, maxPath(node.right))
        
        mx[0] = max(mx[0], node.val + left_sum + right_sum)
        
        return node.val + max(left_sum, right_sum)
    
    maxPath(root)
    
    return mx[0]

#########################################################################################################################

########################################################################################################
## ** Binary Tree: Maximum subset sum **
## Given a binary tree with a value associated with each node, we need to choose a subset of these nodes such that sum of chosen nodes is maximum 
## under a constraint that no two chosen node in subset should be directly connected that is, if we have taken a node in our sum then 
## we can’t take its any children or parents in consideration and vice versa.

def maxSubsetSum(root: TreeNode) -> int:
    mx = [0]
    
    def solver(root):
        ## base case
        if root is None:
            return (0, 0)
        
        left_incl, left_excl = solver(root.left)
        right_incl, right_excl = solver(root.right)
        
        incl = root.val + left_excl + right_excl
        excl = max(left_incl, left_excl) + max(right_incl, right_excl)
        
        mx[0] = max(mx[0], max(incl, excl))
        
        return (incl, excl)
    
    solver(root)
    
    return mx[0]


## build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.right.right = TreeNode(6)

mx_sum = maxSubsetSum(root)
print(mx_sum)



root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.left.right = TreeNode(6)



# root = TreeNode(2)
# root.left = TreeNode(-1)

# # has_path = pathSumI(root, 22)
# # print(has_path)

# # all_paths = pathSumII(root, 22)
# # print(all_paths)

# # print(pathSumIII(root, 22))

# maxSum = maxPathSum(root)
# print(maxSum)