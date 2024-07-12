from collections import deque

class Node:
    
    def __init__(self, val, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


## **Tree traversals**

def dfs(root: Node):
    ## base case
    if root is None:
        return
    
    dfs(root.left)
    print(root.val, end=' ')
    dfs(root.right)
    
    return

def bfs(root: Node):
    if root is None:
        return
    
    curr = root
    
    while curr:
        hold = curr
        
        while curr:
            print(curr.val, end=' ')
            
            curr = curr.next
        
        curr = hold.left
    
    return


## **116. Populating Next Right Pointers in Each Node**
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
        
def connect1(root: Node) -> Node:
    
    def solver(root):
        if root is None:
            return None
    
        curr = root
        
        while curr.left:
            hold = curr
            
            while curr:
                curr.left.next = curr.right
                curr.right.next = curr.next.left if curr.next else None
                
                curr = curr.next
            
            curr = hold.left
        
        return root
    
    return solver(root)
#########################################################################################################################################
## **117. Populating Next Right Pointers in Each Node II**
# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

def connect2(root: Node) -> Node:
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    
    while queue:
        n = len(queue)
        prev = None
        
        for _ in range(n):
            curr = queue.popleft()
            
            curr.next = prev
            prev = curr
            
            if curr.right:
                queue.append(curr.right)
            
            if curr.left:
                queue.append(curr.left)
    
    return root


## building a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root = connect2(root)

## dfs
dfs(root)

print()

## bfs
bfs(root)