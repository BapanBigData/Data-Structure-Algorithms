import math

class TreeNode:
    
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


## to build the tree
## insert at BST
def insert(root: TreeNode, x: int) -> TreeNode:
    node = TreeNode(x)
    
    if root is None:
        return node
    
    if root.val == x:
        return root
    
    if x > root.val:
        root.right = insert(root.right, x)
    else:
        root.left = insert(root.left, x)
    
    return root


## k-th smallest is BST
def printKthSmallest(root, k):
    cnt = [0]
    
    def solver(root, k):
        if root is None:
            return
        
        solver(root.left, k)
        cnt[0] += 1
        
        if cnt[0] == k:
            print(root.val, end=' ')
            return
        
        solver(root.right, k)
        return
    
    return solver(root, k)


def isValidBST(root) -> bool:
    
    def getMaxVal(root):
        if root is None:
            return -math.inf
        
        res = root.val
        left = getMaxVal(root.left)
        right = getMaxVal(root.right)
        
        if left > res:
            res = left
        
        if right > res:
            res = right
        
        return res
    
    def getMinVal(root):
        if root is None:
            return math.inf
        
        res = root.val
        left = getMinVal(root.left)
        right = getMinVal(root.right)
        
        if left < res:
            res = left
        
        if right < right:
            res = right
        
        return res
    
    def naiveSolver(root):
        if root is None:
            return True
        
        if root.left and (root.val <= getMaxVal(root.left)):
            return False
        
        if root.right and (root.val >= getMinVal(root.right)):
            return False
        
        if not naiveSolver(root.left) or not naiveSolver(root.right):
            return False
        
        return True
    
    mp = {}
    
    def traversal(root):
        if root is None:
            return
        
        mp[root] = getMaxVal(root.left), getMinVal(root.right)
        traversal(root.left)
        traversal(root.right)
        return
    
    def solver(root):
        if root is None:
            return True
        
        if root.val <= mp[root][0]:
            return False
        
        if root.val >= mp[root][-1]:
            return False
        
        if not solver(root.left) or not solver(root.right):
            return False
        
        return True
    
    traversal(root)
    
    return solver(root)


def isValidBST1(root):
    
    def getMaxMinVal(root, mp):
        if root is None:
            return -math.inf, math.inf

        left_max, left_min = getMaxMinVal(root.left, mp)
        right_max, right_min = getMaxMinVal(root.right, mp)

        # Store the values into the dict
        mp[root] = (left_max, right_min)

        max_val = max(root.val, max(left_max, right_max))
        min_val = min(root.val, min(left_min, right_min))

        return max_val, min_val
    
    def solver(root, mp):
        if root is None:
            return True
        
        if root.val <= mp[root][0]:
            return False
        
        if root.val >= mp[root][-1]:
            return False
        
        if not solver(root.left, mp) or not solver(root.right, mp):
            return False
        
        return True
    
    ## most efficient soln
    def solveEfficient(root, lower, upper):
        if root is None:
            return True
        
        return (root.val > lower) and (root.val < upper) and \
            solveEfficient(root.left, lower, root.val) and solveEfficient(root.right, root.val, upper)
    
    return solveEfficient(root, -math.inf, math.inf)


## let's build the tree
root = None
values = [50, 20, 100, 10, 40, 70, 120, 60, 80]
for val in values:
    root = insert(root, val)


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)

    
# print(root.left.left.val)
# printKthSmallest(root, 3)
print(isValidBST1(root))

print(isValidBST(root))
