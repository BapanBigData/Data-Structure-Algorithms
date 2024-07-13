# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def printList(head: Node):
    curr = head
    while curr:
        print(f"Node {curr.val} -> {(curr.next.val if curr.next else None, curr.random.val if curr.random else None)}")
        curr = curr.next
    print()
    return 


## **138. Copy List with Random Pointer**

def cloneRandomList(head: Node) -> Node:
    ## let's initialize a dict
    mp = {}
    
    curr = head
    while curr:
        
        newNode = Node(curr.val)
        mp[curr] = newNode
        
        curr = curr.next
    
    curr = head
    while curr:
        
        cloned_node = mp[curr]
        cloned_node.next = mp.get(curr.next, None)
        cloned_node.random = mp.get(curr.random, None)
        
        curr = curr.next
    
    return mp.get(head, None)


def cloneRandomList1(head: Node) -> Node:
    ## 1. insert clone nodes in between
    curr = head
    while curr:
        cloned_node = Node(curr.val)
        cloned_node.next = curr.next
        curr.next = cloned_node
        curr = curr.next.next
    
    ## 2. connect the random pointer
    curr = head
    while curr:
        cloned_node = curr.next
        cloned_node.random = curr.random.next if curr.random else None
        curr = curr.next.next
    
    ##3. connect the next pointer and extract the list out
    dNode = Node(-1)
    res = dNode
    curr = head
    while curr:
        res.next = curr.next
        curr.next = curr.next.next
        res = res.next
        curr = curr.next
    
    cloned_head = dNode.next
    dNode.next = None
    
    return cloned_head


## build the list

## next pointers
l = Node(7)
l.next = Node(13)
l.next.next = Node(11)
l.next.next.next = Node(4)
l.next.next.next.next = Node(1)

## random pointers
l.random = None
l.next.random = l
l.next.next.random = l.next.next.next.next
l.next.next.next.random = l.next.next
l.next.next.next.next.random = l.next 

printList(l)

cloned = cloneRandomList1(l)
printList(cloned)