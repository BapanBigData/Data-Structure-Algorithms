class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.prev = None
        
        
def factorial_large_number(tail, n):
    temp = tail
    prevNode = tail
    carry = 0
    
    while temp:
        data = temp.data * n + carry
        temp.data = data % 10
        carry = data // 10
        prevNode = temp
        temp = temp.prev
    
    while carry != 0:
        prevNode.prev = Node(int(carry % 10))
        carry = carry // 10
        prevNode = prevNode.prev
    
    return

def print_linked_list(tail):
    if not tail:
        return
    print_linked_list(tail.prev)
    print(tail.data, end='')


## Driver code
n = 21
tail = Node(1)
for i in range(2, n+1):
    factorial_large_number(tail, i)

print_linked_list(tail)