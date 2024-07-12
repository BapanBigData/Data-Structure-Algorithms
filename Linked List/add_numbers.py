class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def printList(head: Node):
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
        
    print()
    return

## **2. Add Two Numbers**
## You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
## and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
## You may assume the two numbers do not contain any leading zero, except the number 0 itself.
def addTwoNumbers(l1: Node, l2: Node) -> Node:
    temp1, temp2 = l1, l2
    dummyNode = Node(-1)
    curr = dummyNode
    carry = 0
    
    while temp1 or temp2:
        s = carry
        
        if temp1:
            s = s + temp1.val
        
        if temp2:
            s = s + temp2.val
        
        newNode = Node(s % 10)
        carry = s // 10
        
        curr.next = newNode
        curr = curr.next
        
        if temp1:
            temp1 = temp1.next
        
        if temp2:
            temp2 = temp2.next
            
    if carry:
        curr.next = Node(carry)
    
    head = dummyNode.next
    dummyNode.next = None
    
    return head

# ## build the linked list
# l1 = Node(3)
# l1.next = Node(5)

# l2 = Node(4)
# l2.next = Node(5)
# l2.next.next = Node(9)
# l2.next.next.next = Node(9)

# head = addTwoNumbers(l1, l2)
# printList(head)

############################################################################################################################
## **Add one to given Linked List**
## **Amazon Interview Question**

def addOne(l: Node) -> Node:
    
    def reverse(head):
        ## base case
        if head is None or head.next is None:
            return head
        
        rev_head = reverse(head.next)
        rev_tail = head.next
        
        rev_tail.next = head
        head.next = None
        
        return rev_head
    
    head = reverse(l)
    prev = None
    curr = head
    carry = 1
    
    while curr:
        s = carry
        s = s + curr.val
        
        curr.val = s % 10
        carry = s // 10
        
        prev = curr
        curr = curr.next
    
    if carry:
        newNode = Node(carry)
        prev.next = newNode
    
    req_head = reverse(head)
    
    return req_head


def addOne1(l: Node) -> Node:
    ## to reverse the list
    def reverse(head):
        ## base case
        if head is None or head.next is None:
            return head
        
        rev_head = reverse(head.next)
        rev_tail = head.next
        
        rev_tail.next = head
        head.next = None
        
        return rev_head
    
    head = reverse(l)
    curr = head
    carry = 1
    
    while curr:
        curr.val = curr.val + carry
        
        if curr.val < 10:
            carry = 0
            break
        else:
            curr.val = 0
            carry = 1
        
        curr = curr.next
    
    req_head = reverse(head)
    
    if carry:
        newNode = Node(carry)
        newNode.next = req_head
        return newNode
    
    return req_head


## **bracktracking soln (single traversal efficient soln)**

def addOne2(head: Node) -> Node:
    
    def solver(curr):
        ## base case
        if curr is None:
            return 1
        
        carry = solver(curr.next)
        curr.val = curr.val + carry
        
        if curr.val < 10:
            return 0
        
        curr.val = 0
        
        return 1 
    
    carry = solver(head)
    
    if carry:
        newNode = Node(carry)
        newNode.next = head
        return newNode
    
    return head


## build the list
l = Node(9)
l.next = Node(9)
l.next.next = Node(9)
l.next.next.next = Node(1)
l.next.next.next.next = Node(0)

head = addOne2(l)
printList(head)