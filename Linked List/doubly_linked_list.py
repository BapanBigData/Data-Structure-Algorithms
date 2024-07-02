class Node:
    
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class TreeNode:
    
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right



def printList(head: Node):
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
        
    print()
    return


def insertAtBeginning(head: Node, x):
    newNode = Node(x)
    
    if head is None:
        return newNode
    
    newNode.next = head
    head.prev = newNode
    
    return newNode


def insertAtEnd(head: Node, x):
    newNode = Node(x)
    
    if head is None:
        return newNode
    
    curr = head
    while curr.next:
        curr = curr.next
    
    curr.next = newNode
    newNode.prev = curr
    
    return head


def reverseDLL(head: Node):
    if head is None or head.next is None:
        return head
    
    prv = None
    curr = head
    while curr:
        prv = curr
        
        ## swap the prev and next of the curr node
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    
    return prv
##########################################################################################################################
## Convert binary tree to DLL (inplace):




node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# printList(node1)

lst = [2, 3, 5, 9, 0, 4, 6]
head1 = None
head2 = None 
for e in lst:
    head1 = insertAtBeginning(head1, e)
    head2 = insertAtEnd(head2, e)
    
# printList(head1)
printList(head2)

head = reverseDLL(head2)
printList(head)