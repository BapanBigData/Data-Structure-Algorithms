class Node:
    
    def __init__(self, val) -> None:
        self.value = val
        self.next = None


def printList(head: Node):
    curr = head
    while curr is not None:
        print(curr.value, end=' ')
        curr = curr.next
        
    print()
    return

## insert at the end of of linked list
def insertAtEnd(head: Node, x: int):
    newNode = Node(x)
    if head is None:
        return newNode
    
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = newNode
    
    return head


def reverseListInGroups(head: Node, k: int):
    ## base case
    if head == None or head.next == None:
        return head
    
    cnt = 1
    prev, nxt = None, None
    curr = head
    while curr and cnt <= k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
        cnt += 1
    
    rev_head = reverseListInGroups(curr, k)
    head.next = rev_head
    
    return prev


def detectLoop(head: Node):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def detectRemoveLoop(head: Node):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    if slow != fast:
        return
    
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    
    fast.next = None
    return

def cntNodes(head: Node):
    cnt = 0
    curr = head
    while curr:
        cnt += 1
        curr = curr.next
    
    return cnt

## assumption: the length of list1 >= length of the list2
def getIntersection(h1: Node, h2: Node):
    s = set()
    curr = h1
    while curr:
        s.add(curr)
        curr = curr.next
    
    curr = h2
    while curr:
        if curr in s:
            return curr.value
        curr = curr.next
    
    return -1


def getIntersection1(h1: Node, h2: Node):
    cnt1 = cntNodes(h1)
    cnt2 = cntNodes(h2)
    
    d = abs(cnt1 - cnt2)
    curr1, curr2 = h1, h2
    
    for _ in range(d):
        if curr1 == None:
            return -1
        
        curr1 = curr1.next
    
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1.value
        
        curr1 = curr1.next
        curr2 = curr2.next
    
    return -1


def segregateEvenOdd(head: Node):
    es, ee, os, oe = None, None, None, None
    
    curr = head
    while curr:
        ## if it is even
        if curr.value % 2 == 0:
            if es == None:
                es = curr
                ee = es
            else:
                ee.next = curr
                ee = ee.next
        else:
            if os == None:
                os = curr
                oe = os
            else:
                oe.next = curr
                oe = oe.next
        
        curr = curr.next
    
    ## edge cases
    if (es == None) or (os == None):
        return head
    
    ee.next = os
    oe.next = None
    
    return es


def pairWiseSwap(head: Node):
    ## base case
    if head ==  None or head.next == None:
        return head
    
    cnt = 1
    prev = None
    curr = head
    while curr and cnt <= 2:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
        cnt += 1
    
    rev_head = pairWiseSwap(curr)
    head.next = rev_head
    
    return prev


def naivePairWiseSwap(head: Node):
    curr = head
    while curr and curr.next:
        ## swap the values
        curr.value, curr.next.value = curr.next.value, curr.value
        
        curr = curr.next.next
    
    return head


def mergeTwoSortedList(h1: Node, h2: Node):
    ## handle edge cases
    if h1 == None:
        return h2
    
    if h2 == None:
        return h1
    
    a, b = h1, h2
    head, tail = None, None
    
    if a.value <= b.value:
        head = tail = a
        a = a.next
    else:
        head = tail = b
        b = b.next
    
    while a and b:
        if a.value <= b.value:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    
    if a != None:
        tail.next = a
    else:
        tail.next = b
    
    return head


## palindrome linked list
def naiveIsPalindromList(head: Node):
    stack = []
    curr = head
    while curr:
        stack.append(curr.value)
        
        curr = curr.next
    
    curr = head
    while curr:
        if curr.value != stack.pop():
            return False
        
        curr = curr.next
    
    return True


def reverseList(head: Node):
    ## base case
    if head == None or head.next == None:
        return head
    
    rev_head = reverseList(head.next)
    rev_tail = head.next
    rev_tail.next = head
    head.next = None
    
    return rev_head


def isPalindromList(head: Node):
    if head == None:
        return True
    
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    rev_head = reverseList(slow.next)
    curr = head
    
    while rev_head is not None:
        if curr.value != rev_head.value:
            return False
        
        curr = curr.next
        rev_head = rev_head.next
    
    return True


def reOrderList(head: Node):
    ## edge cases
    if not head or not head.next:
        return
    
    prev = None
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = None
    rev_head = reverseList(slow)
    
    return head, rev_head




lst = [1, 2, 3, 4, 5]
h = None
for e in lst:
    h = insertAtEnd(h, e)

printList(h)

head, rev_head = reOrderList(h)

printList(head)
printList(rev_head)


# ## code to build the sorted lists
# lst1 = [10, 20, 30, 40]
# lst2 = [5, 15, 17, 18, 35]

# h1, h2 = None, None

# for e in lst1:
#     h1 = insertAtEnd(h1, e)

# for f in lst2:
#     h2 = insertAtEnd(h2, f)
    
# printList(h1)
# printList(h2)
    
# head = mergeTwoSortedList(h1, h2)
# printList(head)


# ## code to build linked list
# head = None
# lst = [0, 2]

# for e in lst:
#     head = insertAtEnd(head, e)

# printList(head)

# head = pairWiseSwap(head)
# printList(head)

# head = segregateEvenOdd(head)
# printList(head)



## build the linked list
# head = Node(5)
# head.next = Node(8)
# head.next.next = Node(7)
# head.next.next.next = Node(10)
# head.next.next.next.next = Node(12)
# head.next.next.next.next.next = Node(15)

# head1 = Node(9)
# head1.next = Node(8)
# head1.next.next = Node(5)
# head1.next.next.next = head.next.next.next

# print(getIntersection1(head, head1))


## build the linked list
# head = Node(10)
# head.next = Node(12)
# head.next.next = Node(15)
# head.next.next.next = Node(20)
# head.next.next.next.next = Node(25)
# head.next.next.next.next.next = head.next

# print(detectLoop(head)) 

# detectRemoveLoop(head)
# print(detectLoop(head))
# printList(head)

# head = reverseListInGroups(head, 3)
# printList(head)