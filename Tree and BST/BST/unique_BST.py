class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
## inorder traversal
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
################################################################################################
## **96. Unique Binary Search Trees**
def numTrees(n: int) -> int:
    
    def solver(n):
        ## base cases
        if n == 0 or n == 1:
            return 1
        
        ans = 0
        for i in range(1, n+1):
            ans += solver(i-1) * solver(n-i)
        
        return ans
    
    return solver(n)

# n = 5
# trees = numTrees(n)
# print(trees)

################################################################################################
## **95. Unique Binary Search Trees II**
## Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. 
## Return the answer in any order.

def generateTrees(n: int) -> list[TreeNode]:
    if n == 0:
        return []
    
    def solver(start, end):
        ## base cases
        if start == end:
            return [TreeNode(start)]
        
        if start > end:
            return [None]
        
        all_trees = []
        
        for i in range(start, end+1):
            left_trees = solver(start, i-1)
            right_trees = solver(i+1, end)
            
            for left in left_trees:
                for right in right_trees:
                    curr_root = TreeNode(i)
                    curr_root.left = left
                    curr_root.right = right
                    all_trees.append(curr_root)
        
        return all_trees
    
    return solver(1, n)

n = 4
roots = generateTrees(n)
# print(roots) 

for root in roots:
    preOrderTraversal(root)
    print()