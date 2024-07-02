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

def search(head: Node, target: int):
    pos = 1
    curr = head
    while curr:
        if curr.value == target:
            return pos
        
        curr = curr.next
        pos += 1
    
    return -1


## insert at the begging of the linked list
def insertAtBeginning(head: Node, x: int):
    newNode = Node(x)
    newNode.next = head
    head = newNode
    
    return head

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

## insert at the given position
def insertAtPos(head: Node, x: int, pos: int):
    newNode = Node(x)
    if pos == 1:
        newNode.next = head
        return newNode
    
    cnt = 1
    curr = head
    while curr:
        if cnt == pos-1:
            temp = curr.next
            curr.next = newNode
            newNode.next = temp
            break
        
        cnt += 1
        curr = curr.next
    
    return head


def deleteFirstNode(head: Node):
    if head == None:
        return None
    
    return head.next


def deleteLastNode(head: Node):
    if head == None or head.next == None:
        return None
    
    curr = head
    while curr.next.next:
        curr = curr.next
    
    curr.next = None
    return head


## the node to be deleted is never be the last node
def deleteNodeWithGivenPointer(ptr: Node):
    temp = ptr.next
    ptr.value = temp.value
    ptr.next = temp.next
    
    return


def sortedInsert(head: Node, x: int):
    newNode = Node(x)
    
    if x < head.value or head == None:
        newNode.next = head
        return newNode
    
    curr = head
    while curr.next:
        if x < curr.next.value:
            temp = curr.next
            curr.next = newNode
            newNode.next = temp
            break
        
        curr = curr.next
    
    if curr.next == None:
        curr.next = newNode
        newNode.next = None
    
    return head

## efficient approach
def printMiddle(head: Node):
    if head == None:
        print(head)
        return
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    print(slow.value)
    return


def printNthNodeFromEnd(head: Node, n: int):
    l = 0
    curr = head
    while curr:
        l += 1
        curr = curr.next
    
    if n > l:
        print(None)
        return
        
    curr = head
    for _ in range(l-n):
        curr = curr.next
    
    print(curr.value)
    return 

## efficient
def printNthNodeFromEnd1(head: Node, n: int):
    first = head
    for _ in range(n):
        if first == None:
            print(first)
            return 
        
        first = first.next
    
    second = head
    while first and second:
        first = first.next
        second = second.next
    
    print(second.value)
    return


def removeSortedDuplicates(head: Node):
    
    curr = head
    while curr and curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head


def reverseList(head: Node):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev


def reverseList1(head: Node):
    ## base case
    if head == None or head.next == None:
        return head
    
    rev_head = reverseList1(head.next)
    rev_tail = head.next
    rev_tail.next = head
    head.next = None
    
    return rev_head


head = None
lst = [1, 3, 5, 2, 0, 8, 4, 9, 6, 7]

for e in lst:
    head = insertAtEnd(head, e)

printList(head)

head = reverseList1(head)
printList(head)

# head = removeSortedDuplicates(head)
# printList(head)

## linked list
# head = Node(5)
# head.next = Node(3)
# # head.next.value = 9
# head.next.next = Node(2)
# head.next.next.next = Node(7)
# head.next.next.next.next = Node(10)

# printList(head)

# deleteNodeWithGivenPointer(ptr=head)
# printList(head)

# ## print the above list
# printList(head)
# print(search(head, 2))

# head = None
# head = insertAtBeginning(head, 1)
# head = insertAtBeginning(head, 5)
# head = insertAtBeginning(head, 0)
# head = insertAtBeginning(head, 7)
# head = insertAtBeginning(head, 10)

# head = None
# lst = [10, 20, 30, 40, 50, 60, 70]

# for e in lst:
#     head = insertAtEnd(head, e)
    
# # head = insertAtEnd(head, 1)
# # head = insertAtEnd(head, 3)
# # head = insertAtEnd(head, 6)
# # head = insertAtEnd(head, 0)
# # head = insertAtEnd(head, 10)

# printList(head)

# printNthNodeFromEnd1(head, 6)

# printList(head)

# head = insertAtPos(head, x=100, pos=5)
# printList(head)

# head = deleteFirstNode(head)
# printList(head)

# head = deleteLastNode(head)
# printList(head)

# head = sortedInsert(head, x=1)
# printList(head) 
# printMiddle(head)