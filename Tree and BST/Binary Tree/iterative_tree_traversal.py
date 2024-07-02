class TreeNode:
    
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


## Iterative inorder traversal
def printInOrderTraversal(root: TreeNode) -> None:
    if root is None:
        return
    
    stack = []
    
    curr = root
    while curr:
        stack.append(curr)
        curr = curr.left
    
    while stack:
        top = stack.pop()
        print(top.val, end=' ')
        
        curr = top.right
        while curr:
            stack.append(curr)
            curr = curr.left
    
    return


## iterative preorder traversal
def printPreOrderTraversal(root: TreeNode) -> None:
    if root is None:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        curr = stack.pop()
        print(curr.val, end=' ')
        
        if curr.right:
            stack.append(curr.right)
        
        if curr.left:
            stack.append(curr.left)
    
    return


def printPreOrderTraversalOptSpace(root: TreeNode) -> None:
    if root is None:
        return 
    
    stack = []
    
    curr = root
    while curr or stack:
        while curr:
            print(curr.val, end=' ')
            
            if curr.right:
                stack.append(curr.right)
            
            curr = curr.left
        
        if stack:
            curr = stack.pop()
            
    return 


## let's build the tree
root = TreeNode(30)
root.left = TreeNode(40)
root.right = TreeNode(50)
root.left.left = TreeNode(100)
root.right.left = TreeNode(70)
root.right.right = TreeNode(80)

printInOrderTraversal(root)
print()
printPreOrderTraversal(root)
print()
printPreOrderTraversalOptSpace(root)