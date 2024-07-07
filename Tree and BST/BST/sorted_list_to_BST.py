class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
        
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#################################################################
def printList(head: ListNode):
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
        
    print()
    return

## inorder traversal
def inOrderTraversal(root: TreeNode):
    ## base case
    if root is None:
        return
    
    inOrderTraversal(root.left)
    print(root.val, end=' ')
    inOrderTraversal(root.right)
    
    return

## **109. Convert Sorted List to Binary Search Tree**
## Given the head of a singly linked list where elements are sorted in ascending order, convert it to a `height-balanced` binary search tree.
def sortedListToBST(head: ListNode) -> TreeNode:
    
    def convertToBST(start, end):
        ## base case
        if start == end:
            return None
        
        slow, fast = start, start
        
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.val)
        root.left = convertToBST(start, slow)
        root.right = convertToBST(slow.next, end)
        
        return root
    
    if head is None:
        return None
    
    return convertToBST(head, None)


## let's build the list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

printList(head)

root = sortedListToBST(head)

inOrderTraversal(root)