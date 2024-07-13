from collections import deque, OrderedDict
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

## level order traversal line by line

def levelOrderTraversalLineByLine(root: TreeNode):
    if root is None:
        return
    
    q = deque()
    q.append(root)
    q.append(None)
    
    while len(q) > 1:
        curr = q.popleft()
        
        if curr == None:
            print()
            q.append(None)
            continue
        
        print(curr.val, end=' ')
        
        if curr.left is not None:
            q.append(curr.left)
        
        if curr.right is not None:
            q.append(curr.right)
    
    return


def levelOrderTraversalLineByLine1(root: TreeNode):
    if root is None:
        return
    
    q = deque()
    q.append(root)
    
    while q:
        
        cnt = len(q)
        
        for _ in range(cnt):
            curr = q.popleft()
            print(curr.val, end=' ')
            
            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
            
        print()
    
    return

#################################################################################################################
## check the given tree height balanced
def heightOfTree(root: TreeNode):
    ## base cases
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    leftTree = heightOfTree(root.left)
    rightTree = heightOfTree(root.right)
    
    return max(leftTree, rightTree) + 1


def isHeightBalancedBrutForce(root: TreeNode):
    ## base cases
    if root is None:
        return True
    
    if not root.left and not root.right:
        return True
    
    lh = heightOfTree(root.left)
    rh = heightOfTree(root.right)
    
    return abs(lh-rh) <= 1 and isHeightBalancedBrutForce(root.left) and isHeightBalancedBrutForce(root.right)


def isHeightBalanced(root: TreeNode) -> bool:
    
    def solver(root):
        ## base cases
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        lh = solver(root.left)
        
        if lh == -1:
            return -1
        
        rh = solver(root.right)
        
        if rh == -1:
            return -1
        
        if abs(lh-rh) > 1:
            return -1
        
        return max(lh, rh) + 1
    
    res = solver(root)
    
    return False if res == -1 else True

############################################################################################################################
## let's print the horizontal distance of every node of the given binary tree
def printHorizontalDistance(root: TreeNode):
    if root is None:
        return 
    
    ## in the queue it's in the form of (node, hd)
    q = deque()
    q.append([root, 0])
    
    while q:
        curr, hd = q.popleft()
        
        print(f"node {curr.val} : hd {hd}")
        
        if curr.left:
            q.append([curr.left, hd-1])
        
        if curr.right:
            q.append([curr.right, hd+1])
    
    return


def topView(root: TreeNode) -> list[int]:
    if root is None:
        return []
    
    ## initializing a queue and a dict
    q = deque()
    
    ## OrderedDict preserves insertion order, but normal dicts may not.
    ## Here, we don't bother about insertion order, but we do care about the sorted order of the keys. 
    ## Unfortunately, Python doesn't provide any built-in data structure that directly serves our purpose here.
    ## Therefore, we can go for either OrderedDict() or dict(). At last, we have to return the result 
    ## based on the sorted order of the keys (e.g., hd).
    hd_mp = OrderedDict()
    
    q.append([0, root])
    
    while q:
        hd, curr = q.popleft()
        
        if hd not in hd_mp:
            hd_mp[hd] = curr.val
        
        if curr.left:
            q.append([hd-1, curr.left])
        
        if curr.right:
            q.append([hd+1, curr.right])
    
    return [hd_mp[key] for key in sorted(hd_mp.keys())]


def bottomView(root: TreeNode) -> list[int]:
    if root is None:
        return []
    
    ## initializing a queue and a dict
    q = deque()
    
    ## OrderedDict preserves insertion order, but normal dicts may not.
    ## Here, we don't bother about insertion order, but we do care about the sorted order of the keys. 
    ## Unfortunately, Python doesn't provide any built-in data structure that directly serves our purpose here.
    ## Therefore, we can go for either OrderedDict() or dict(). At last, we have to return the result 
    ## based on the sorted order of the keys (e.g., hd).
    hd_mp = OrderedDict()
    
    q.append([0, root])
    
    while q:
        hd, curr = q.popleft()
        
        hd_mp[hd] = curr.val
        
        if curr.left:
            q.append([hd-1, curr.left])
        
        if curr.right:
            q.append([hd+1, curr.right])
    
    return [hd_mp[key] for key in sorted(hd_mp.keys())]


def verticalTraversal(root: TreeNode):
    if root is None:
        return []
    
    q = deque()
    hd_mp = {}
    
    q.append([0, root])
    
    while q:
        hd, curr = q.popleft()
        
        if hd not in hd_mp:
            hd_mp[hd] = []
        
        hd_mp[hd].append(curr.val)
        
        if curr.left:
            q.append([hd-1, curr.left])
        
        if curr.right:
            q.append([hd+1, curr.right])
    
    return [e for key in sorted(hd_mp.keys()) for e in hd_mp[key]]

############################################################################################################################
## Maximum Width of the given binary tree:
def maxWidth(root: TreeNode):
    if root is None:
        return 0
    
    w = -math.inf
    
    ## initializing a queue
    q = deque()
    q.append(root)
    
    while q:
        cnt = len(q)
        w = max(w, cnt)
        
        for _ in range(cnt):
            curr = q.popleft()
            
            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
    
    return w
###################################################################################################################################
## flatten the given binary tree
prev, head = None, None

def inOrderFlattenToDLL(root: TreeNode):
    global prev, head
    
    if root is None:
        return
    
    inOrderFlattenToDLL(root.left)
    
    if prev is None:
        head = root
    else:
        root.left = prev
        prev.right = root
    
    prev = root
    
    inOrderFlattenToDLL(root.right)
    return


def inOrderFlattenToDLL1(root: TreeNode):
    
    def solver(root, prev, head):
        ## base case
        if root is None:
            return
        
        solver(root.left, prev, head)
        
        if prev[0] is None:
            head[0] = root
        else:
            root.left = prev[0]
            prev[0].right = root
        
        prev[0] = root
        
        solver(root.right, prev, head)
        return
    
    prev = [None]
    head = [None]
    
    solver(root, prev, head)
    
    return head[0]

## Error: RecursionError: maximum recursion depth exceeded
# def preOrderFlattenTree(root: TreeNode):
    
#     def solver(root, prev, head):
#         ## base case
#         if root is None:
#             return
        
#         if prev[0] is None:
#             head[0] = root
#         else:
#             root.left = prev[0]
#             prev[0].right = root
        
#         prev[0] = root
        
#         solver(root.left, prev, head)
#         solver(root.right, prev, head)
        
#         return
    
#     prev = [None]
#     head = [None]
    
#     solver(root, prev, head)
    
#     return head[0]


def printFlattenTree(head):
    curr = head
    while curr:
        print(curr.val, end=' ')
        curr = curr.right
        
    print()
    return



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

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# head = inOrderFlattenToDLL1(root2)
# printFlattenTree(head)

## level order traversal line by line
# levelOrderTraversalLineByLine(root)
# levelOrderTraversalLineByLine(root1)
# levelOrderTraversalLineByLine(root2)

# print(isHeightBalancedBrutForce(root1))
# print(isHeightBalancedBrutForce(root1))
# print(isHeightBalancedBrutForce(root2))

# print(isHeightBalanced(root1))
# print(isHeightBalanced(root1))
# print(isHeightBalanced(root2))

# root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(1)
# root.right.left = TreeNode(4)
# root.right.left.left = TreeNode(5)
# root.right.left.right = TreeNode(6)

# printHorizontalDistance(root)
# top, bot, ver = topView(root1), bottomView(root1), verticalTraversal(root1)
# print(top)
# print(bot)
# print(ver)