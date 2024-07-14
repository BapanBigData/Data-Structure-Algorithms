class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 


## ** 173. Binary Search Tree Iterator **
## ** Application of iterative inorder traversal **    
## You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)
        
    def pushAll(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        top = self.stack.pop()
        self.pushAll(top.right)
        return top.val

    def hasNext(self) -> bool:
        return True if self.stack else False
    
## building the BST
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

## bst iterator obj
bst_iter = BSTIterator(root)

print(bst_iter.next())    
print(bst_iter.next()) 
print(bst_iter.next()) 
print(bst_iter.hasNext())
print(bst_iter.next())    
print(bst_iter.next()) 
print(bst_iter.hasNext())