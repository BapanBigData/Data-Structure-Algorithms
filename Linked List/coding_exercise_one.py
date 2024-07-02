class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        curr = self.head
        
        while curr:
            print(curr.value, end=' ')
            curr = curr.next
        
        return
    
    def append(self, value):
        
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        
        return True
    
    def pop(self):
        
        if self.length == 0:
            return None
        
        if self.length == 1:
            res = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return res
        
        res = self.tail.value
        curr = self.head
        while curr.next.next:
            curr = curr.next
        self.tail = curr
        self.tail.next = None
        self.length -= 1
        
        return res
    
    def prepend(self, value):
        
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            res = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return res
        
        temp = self.head
        
        self.head = self.head.next
        self.length -= 1
        
        return temp.value
    
    def get(self, pos):
        if pos < 1 or pos > self.length:
            return None
        
        if pos == 1:
            return self.head.value
        
        if pos == self.length:
            return self.tail.value
        
        cnt = 1
        curr = self.head
        
        while curr:
            cnt += 1
            curr = curr.next
            if cnt == pos:
                return curr.value
        
        return None
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Update head and tail
        self.tail = self.head
        self.head = prev
        return
    
    def recursive_reverse(self):
        
        def solver(curr):
            pass
            

my_linked_list = LinkedList(10)
my_linked_list.append(30)
my_linked_list.append(5)
my_linked_list.append(40)
my_linked_list.prepend(1)

print("Head of list:", my_linked_list.head.value)
print("Tail of list:", my_linked_list.tail.value)
print("Length of list:", my_linked_list.length)

my_linked_list.print_list()
print()

# print(my_linked_list.pop_first())

# print("Head of list:", my_linked_list.head.value)
# print("Tail of list:", my_linked_list.tail.value)
# print("Length of list:", my_linked_list.length)

# pos = 3
# print(f"The {pos}th item is:", my_linked_list.get(pos))

print('---------------------')

my_linked_list.reverse()

print("Head of list:", my_linked_list.head.value)
print("Tail of list:", my_linked_list.tail.value)
print("Length of list:", my_linked_list.length)

my_linked_list.print_list()
# print()
# print(my_linked_list.pop())

# print("Head of list:", my_linked_list.head.value)
# print("Tail of list:", my_linked_list.tail.value)
# print("Length of list:", my_linked_list.length)

# print(my_linked_list.pop())

# print("Head of list:", my_linked_list.head.value)
# print("Tail of list:", my_linked_list.tail.value)
# print("Length of list:", my_linked_list.length)

# print(my_linked_list.pop())

# print("Head of list:", my_linked_list.head.value)
# print("Tail of list:", my_linked_list.tail.value)
# print("Length of list:", my_linked_list.length)