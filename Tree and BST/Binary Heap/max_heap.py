import math

class MaxHeap:
    
    def __init__(self, lst=[]) -> None:
        self.heap = lst
        self.sz = len(lst)
        
        ## ** build the heap **
        last_indx = self.sz - 1
        
        i = self.parent(last_indx)
        while i >= 0:
            self.maxHeapify(i)
            i -= 1
    
    def parent(self, i):
        return (i-1) // 2
    
    def leftChild(self, i):
        return (2*i) + 1
    
    def rightChild(self, i):
        return (2*i) + 2
    
    def insert(self, x):
        ## append into the heap
        self.heap.append(x)
        self.sz += 1
        i = self.sz - 1
        while (i > 0) and (self.heap[i] > self.heap[self.parent(i)]):
            p = self.parent(i)
            ## swap
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i] 
            i = p
    
    def extractMax(self):
        if self.sz == 0:
            return -math.inf
        
        res = self.heap[0]
        
        ## swap
        self.heap[0], self.heap[self.sz-1] = self.heap[self.sz-1], self.heap[0]
        
        self.heap.pop()
        self.sz -= 1
        
        ## now, max-heapify the heap
        if self.sz > 0:
            self.maxHeapify(0)
        
        return res
    
    def increaseKey(self, i, x):
        self.heap[i] = x
        
        while (i > 0) and (self.heap[i] > self.heap[self.parent(i)]):
            p = self.parent(i)
            
            ## swap
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
    
    def delete(self, i):
        if (self.sz == 0) or (i >= self.sz):
            return False
        
        self.increaseKey(i, math.inf)
        self.extractMax()
        
        return True
    
    def maxHeapify(self, i):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)
        
        if (left < self.sz) and (self.heap[left] > self.heap[largest]):
            largest = left
        
        if (right < self.sz) and (self.heap[right] > self.heap[largest]):
            largest = right
        
        if largest != i:
            ## swap
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.maxHeapify(largest)
        
        return

# nums = [70, 10, 40, 20, 50, 35, 80]
# max_heap = MaxHeap(nums)
# print(max_heap.heap)

# max_heap.delete(0)
# print(max_heap.heap)
##############################################################################################################
## build max heap

def buildHeap(nums: list[int]) -> None:
    n = len(nums)
    if (n == 0) or (n == 1):
        return
    
    def heapify(i):
        largest = i
        left = (2*i) + 1
        right = (2*i) + 2
        
        if (left < n) and (nums[left] > nums[largest]):
            largest = left
        
        if (right < n) and (nums[right] > nums[largest]):
            largest = right
        
        if (largest != i):
            ## swap
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(largest)
        return
    
    last_indx = n-1
    
    i = (last_indx-1) // 2
    while (i >= 0): 
        heapify(i)
        i -= 1
    
    return

nums = [2, 3, 17, 6, 12, 10, 23, 40, 35, 4, 70, 11, 19, 22, 14, 69, 1, 24]
buildHeap(nums)
print(nums)