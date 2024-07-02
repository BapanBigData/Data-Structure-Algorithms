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

#########################################################################################################################
## Search in Binary Search Tree (BST):
def search(root: TreeNode, x: int) -> bool:
    if root is None:
        return False
    
    if x == root.val:
        return True
    
    if x > root.val:
        return search(root.right, x)
    else:
        return search(root.left, x)
    
    
## iterative search
## T.C: O(logn), Space: O(1)
def iterativeSearch(root: TreeNode, x: int) -> bool:
    while root:
        if root.val == x:
            return True
        
        if x > root.val:
            root = root.right
        else:
            root = root.left
    
    return False


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


## iterative insert
def interativeInsert(root: TreeNode, x: int) -> TreeNode:
    parent = None
    curr = root
    while curr:
        parent = curr
        
        if x == curr.val:
            return root
        
        if x > curr.val:
            curr = curr.right
        else:
            curr = curr.left
            
    node = TreeNode(x)
    
    ## for empty tree
    if parent is None:
        return node
    
    if x > parent.val:
        parent.right = node
    else:
        parent.left = node
    
    return root


## Delete in BST

def getInOrderSuccessor(node: TreeNode) -> int:
    curr = node
    while curr.left:
        curr = curr.left
    
    return curr.val

def delete(root: TreeNode, x: int):
    if root is None:
        return None
    
    if x > root.val:
        root.right = delete(root.right, x)
    elif x < root.val:
        root.left = delete(root.left, x)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = getInOrderSuccessor(root.right)
            root.val = succ
            root.right = delete(root.right, succ)
    
    return root    


## floor in BST
def floor(root: TreeNode, x: int) -> int:
    ans = [None]
    
    def solver(root):
        if root is None:
            return 
        
        if x == root.val:
            ans[0] = x
            return
        
        if x > root.val:
            ans[0] = root.val
            solver(root.right)
        else:
            solver(root.left)
        
        return
    
    solver(root)
    
    return ans[0]


## iterative floor
def iterativeFloor(root, x):
    ans = None
    while root:
        if root.val == x:
            return root.val
        
        if x > root.val:
            ans = root.val
            root = root.right
        else:
            root = root.left
    
    return ans


## ceil in BST
def ceil(root: TreeNode, x: int):
    ans = [None]
    
    def solver(root, x):
        if root is None:
            return
        
        if x == root.val:
            ans[0] = root.val
            return
        
        if x > root.val:
            solver(root.right, x)
        else:
            ans[0] = root.val
            solver(root.left, x)
        
        return 
    
    solver(root, x)
    
    return ans[0]


## iterative ceil fn
def iterativeCeil(root: TreeNode, x: int) -> int:
    ans = None
    while root:
        if root.val == x:
            return root.val
        
        if x > root.val:
            root = root.right
        else:
            ans = root.val
            root = root.left
    
    return ans


## let's build the tree
root = None
values = [20, 15, 30, 40, 50, 12, 18, 35, 80, 7, 2, 11, 8, 9]
for val in values:
    root = insert(root, val)
    
# inOrderTraversal(root)
# print()

# root = delete(root, 20)
# inOrderTraversal(root)

# f = iterativeFloor(root, x=3)
# print(f)

c = iterativeCeil(root, x=5)
print(c)



# ## let's build the tree
# root = TreeNode(20)
# root.left = TreeNode(10)
# root.left.left = TreeNode(5)
# root.right = TreeNode(40)
# root.right.left = TreeNode(30)
# root.right.right = TreeNode(80)
# root.right.right.left = TreeNode(50)
# root.right.right.right = TreeNode(100)

# # inOrderTraversal(root)
# s = iterativeSearch(root, x=5)
# print(s)