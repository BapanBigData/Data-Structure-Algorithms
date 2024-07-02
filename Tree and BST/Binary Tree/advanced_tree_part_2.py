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

########################################################################################################
## Construct binary tree from inorder and preorder traversal
pre_indx = 0
def constructTree(inOrder: list[int], preOrder: list[int]) -> TreeNode:
    
    mp = {}
    for i in range(len(inOrder)):
        mp[inOrder[i]] = i
    
    def solver(insi, inei):
        global pre_indx
        
        if insi > inei:
            return None
        
        root_node = TreeNode(preOrder[pre_indx])
        pre_indx += 1
        
        if insi == inei:
            return root_node
        
        for i in range(insi, inei+1):
            if inOrder[i] == root_node.val:
                break
        
        root_node.left = solver(insi, i-1)
        root_node.right = solver(i+1, inei)
        
        return root_node
    
    
    def efficientSolver(insi, inei):
        global pre_indx
        
        if insi > inei:
            return None
        
        root_node = TreeNode(preOrder[pre_indx])
        pre_indx += 1
        
        if insi == inei:
            return root_node
        
        ## get index of the curr root node in the inorder list
        i = mp[root_node.val]
        
        root_node.left = solver(insi, i-1)
        root_node.right = solver(i+1, inei)
        
        return root_node
    
    return efficientSolver(0, len(inOrder)-1)


# iN = [2, 5, 0, 3, 1]
# pR = [1, 3, 0, 5, 2]

# root = constructTree(inOrder=iN, preOrder=pR)

# inOrderTraversal(root)
# print()
# preOrderTraversal(root)

#####################################################################################################################################
def printZigZagLevelOrder(root: TreeNode):
    
    def solver():
        if root is None:
            return
        
        q = deque()
        q.append(root)
        
        stack = []
        rev_flag = False
        
        while q:
            cnt = len(q)
            
            for _ in range(cnt):
                curr = q.popleft()
                
                if rev_flag:
                    stack.append(curr.val)
                else:
                    print(curr.val, end=' ')
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            if rev_flag:
                while stack:
                    print(stack.pop(), end=' ')
                    
            rev_flag = not rev_flag
            
        return
    
    def solver1():
        if root is None:
            return
        
        stack1 = []
        stack2 = []
        
        stack1.append(root)
        
        while stack1 or stack2:
            
            while stack1:
                curr1 = stack1.pop()
                print(curr1.val, end=' ')
                
                if curr1.left:
                    stack2.append(curr1.left)
                
                if curr1.right:
                    stack2.append(curr1.right)
            
            while stack2:
                curr2 = stack2.pop()
                print(curr2.val, end=' ')
                
                if curr2.right:
                    stack1.append(curr2.right)
                
                if curr2.left:
                    stack1.append(curr2.left)
                    
        return
    
    solver1()
    
    return
#########################################################################################################################
## Diameter of binary tree:
def heightOfTree(root: TreeNode):
    ## base cases
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    leftTree = heightOfTree(root.left)
    rightTree = heightOfTree(root.right)
    
    return max(leftTree, rightTree) + 1


def diameterOfBinaryTree(root: TreeNode) -> int:
    
    def naiveSolver(root):
        ## base cases
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        dia = 1 + heightOfTree(root.left) + heightOfTree(root.right)
        
        left_dia = naiveSolver(root.left)
        right_dia = naiveSolver(root.right)
        
        return max(dia, left_dia, right_dia)
    
    
    ## initializing the memo map, which will map {node -> height}
    height_map = {}
    
    def height_mapping(root):
        ## base cases
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            height_map[root] = 1
            return height_map[root]
        
        height_map[root] = 1 + max(height_mapping(root.left), height_mapping(root.right))
        
        return height_map[root]
    
    
    def solver(root):
        ## base cases
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        ## now, let's calculate the diameter using -> 1 + lh + rh
        dia = 1 + height_map.get(root.left, 0) + height_map.get(root.right, 0)
        
        dia_left = solver(root.left)
        dia_right = solver(root.right)
        
        return max(dia, dia_left, dia_right)
    
    height_mapping(root)
    
    return solver(root)

## let's do the most efficient soln
## we will going to take simillar approach as the problem `check height balanced`
def diameterOfBinaryTree1(root):
    
    dia = [0]
    
    def solver(root):
        ## base cases
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        lh = solver(root.left)
        rh = solver(root.right)
        
        dia[0] = max(dia[0], 1+lh+rh)
        
        return 1 + max(lh, rh)
    
    solver(root)
    
    return dia[0]
###################################################################################################################################
## Lowest Common Ancestor (LCA):
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode: 
    
    def findPath(root, node, path):
        if root is None:
            return False
        
        path.append(root)
        
        if root == node:
            return True
        
        leftTree, rightTree = None, None
        
        if root.left:
            leftTree = findPath(root.left, node, path)
        
        if root.right:
            rightTree = findPath(root.right, node, path)
        
        if leftTree or rightTree:
            return True
        
        path.pop()
        
        return False
    
    path1, path2 = [], []
    
    findPath(root, p, path1)
    findPath(root, q, path2)
    
    i = 0
    while (i < len(path1)) and (i < len(path2)):
        if path1[i] != path2[i]:
            break
        
        i += 1
    
    return path1[i-1]


## efficient soln for LCA
def LCA(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    ## if root is same as p or q we return root
    if (root == p) or (root == q):
        return root
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    
    ## if one of the sub-tree contains p and other sub-tree contains q,
    ## then also we return the root
    if left and right:
        return root
    
    ## finally we return left or right as the function return
    return left if left else right
#####################################################################################################################################################
## Burn a binary tree from a leaf: Time taken to burn the tree from the given leaf
## Note: the below will not work if the leaf = root of the tree
def burnBinaryTree(root: TreeNode, leaf: TreeNode) -> int:
    t = [0]
    
    ## dist[0] sets the distance from the curr node to the given leaf 
    ## if leaf is the descendant of the curr node, the dist[0] will have the distance of root to given leaf
    ## the below function will untimately return the height of the given binary tree.
    def solver(root, leaf, dist):
        if root is None:
            return 0
        
        if root == leaf:
            dist[0] = 0
            return 1
        
        left_dist, right_dist = [-1], [-1]
        
        lh = solver(root.left, leaf, left_dist)
        rh = solver(root.right, leaf, right_dist)
        
        ## if the given leaf is descendant of the left sub-tree
        if left_dist[0] != -1:
            dist[0] = 1 + left_dist[0]
            t[0] = max(t[0], rh + dist[0])
        
        elif right_dist[0] != -1:
            dist[0] = 1 + right_dist[0]
            t[0] = max(t[0], lh + dist[0])
        
        return 1 + max(lh, rh)
    
    dist = [0]
    solver(root, leaf, dist)
    
    return t[0]
#################################################################################################################################
## **2385. Amount of Time for Binary Tree to Be Infected**
## You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
## Explanation of the algo: `https://www.youtube.com/watch?v=1gNbNxbokxc`
## preffered soln over burnBinaryTree()

def amountOfTime(root: TreeNode, start: int) -> int:
    
    t = [0]
    
    def solver(root, start):
        height = 0
        
        if root is None:
            return height
        
        left_height = solver(root.left, start)
        right_height = solver(root.right, start)
        
        if root.val == start:
            t[0] = max(t[0], max(left_height, right_height))
            height = -1
        
        elif (left_height >= 0) and (right_height >= 0):
            height = 1 + max(left_height, right_height)
        
        else:
            dist = abs(left_height) + abs(right_height)
            t[0] = max(t[0], dist)
            
            height = min(left_height, right_height) - 1
        
        return height
    
    solver(root, start)
    
    return t[0]

####################################################################################################################
## Count nodes in a complete binary tree.
## Complete Binary Tree: A binary tree is complete if all levels except possibly the last are fully filled, 
## and all nodes in the last level are filled from left to right.
def countNodes(root: TreeNode) -> int:
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    lh, rh = 0, 0
    
    curr = root
    while curr:
        curr = curr.left
        lh += 1
    
    curr = root
    while curr:
        curr = curr.right
        rh += 1
    
    if lh == rh:
        return (1 << lh) - 1     ## (2 ** lh) - 1
    
    return 1 + countNodes(root.left) + countNodes(root.right)
##################################################################################################################################
## Serialize and Deserialize of a binary tree:
def serializeDeserialize(root: TreeNode):
    
    def serialize(root: TreeNode, arr=[]) -> list[int]:
        ## do the pre-order traversal of the tree
        if root is None:
            arr.append(-1)
            return arr
        
        arr.append(root.val)
        serialize(root.left, arr)
        serialize(root.right, arr)
        
        return arr
    
    i = [0]
    
    def deserialize(arr: list[int]) -> TreeNode:
        if i[0] == len(arr):
            return None
        
        data = arr[i[0]]
        i[0] += 1
        
        if data == -1:
            return None
        
        root = TreeNode(data)
        root.left = deserialize(arr)
        root.right = deserialize(arr)
        
        return root
    
    serialized = serialize(root)
    deserialized = deserialize(serialized)
    
    return serialized, deserialized


## lets build a tree
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)

## left skewed tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)

## let's build a tree
root = TreeNode(10)
root.left = TreeNode(50)
root.right = TreeNode(60)
root.left.left = TreeNode(70)
root.left.left.left = TreeNode(40)
root.left.right = TreeNode(20)
root.left.right.left = TreeNode(90)
root.left.right.left.left = TreeNode(30)
root.left.right.right = TreeNode(80)

serialized, deserialized = serializeDeserialize(root)
print(serialized)
inOrderTraversal(deserialized)
print()
preOrderTraversal(deserialized)


# burn_time = amountOfTime(root, root.val)
# print(burn_time)

# p = root.left.right.left.left
# q = root.left.right.right

# lca = LCA(root, p, q)
# print(lca.val)

# root = TreeNode(2)
# root.right = TreeNode(5)
# root.right.right = TreeNode(0)
# root.right.right.right = TreeNode(3)
# root.right.right.right.right = TreeNode(1)

# root2 = TreeNode(10)
# # root2.left = TreeNode(20)
# # root2.right = TreeNode(30)
# # root2.left.left = TreeNode(8)
# # root2.left.right = TreeNode(7)
# # root2.left.right.left = TreeNode(9)
# # root2.left.right.right = TreeNode(15)
# # root2.right.right = TreeNode(6)

# # printZigZagLevelOrder(root2)
# dia = diameterOfBinaryTree1(root)
# print(dia)

# inOrderTraversal(root)
# print()
# preOrderTraversal(root)