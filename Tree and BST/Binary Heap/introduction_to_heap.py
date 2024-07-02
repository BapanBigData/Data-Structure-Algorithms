import math

class MinHeap:
    
    def __init__(self, lst) -> None:
        self.heap = lst
        self.size = len(lst)
        
        ## **building heap**
        ## index of last node
        last_indx = len(lst) - 1
        
        ## get the parent of `last_index`
        i = self.parent(last_indx)
        while i >= 0:
            self.minHeapify(i)
            i -= 1 
    
    def parent(self, i):
        return (i - 1) // 2
    
    def leftChild(self, i):
        return (2 * i) + 1
    
    def rightChild(self, i):
        return (2 * i) + 2
    
    def insert(self, x):
        ## append in a heap
        self.heap.append(x)
        self.size += 1
        i = self.size - 1
        
        while (i > 0) and (self.heap[self.parent(i)] > self.heap[i]):
            p = self.parent(i)
            ## swap
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            
        return
    
    def extractMin(self):
        ## for empty heap
        if self.size == 0:
            return math.inf
        
        res = self.heap[0]
        
        ## swap the 0-th and n-1
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        
        ## now, pop from the heap
        self.heap.pop()
        
        self.size -= 1
        
        ## now, min-heapify the heap
        self.minHeapify(0)
        
        return res 
    
    def minHeapify(self, i):
        left = self.leftChild(i)
        right = self.rightChild(i)
        smallest = i
        
        if (left < self.size) and (self.heap[left] < self.heap[smallest]):
            smallest = left
        
        if (right < self.size) and (self.heap[right] < self.heap[smallest]):
            smallest = right
        
        if smallest != i:
            ## swap
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.minHeapify(smallest)
        
        return
    
    def decreaseKey(self, i, x):
        self.heap[i] = x
        
        while (i > 0) and (self.heap[self.parent(i)] > self.heap[i]):
            p = self.parent(i)
            
            ## swap
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
        
        return
    
    def delete(self, i):
        if (self.size == 0) or (i >= self.size):
            return 
        
        ## swap
        self.heap[i], self.heap[self.size-1] = self.heap[self.size-1], self.heap[i]
        
        self.heap.pop()
        
        self.size -= 1
        
        ## check if i is 0
        if i == 0:
            self.minHeapify(0)
            return
        
        while (i > 0) and (self.heap[self.parent(i)] > self.heap[i]):
            p = self.parent(i)
            
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            
        return
    
    def delete1(self, i):
        if (self.size == 0) or (i >= self.size):
            return 
        
        self.decreaseKey(i, -math.inf)
        self.extractMin()
        return


# min_heap = MinHeap(lst=[20, 50, 25, 10, 15, 40, 100, 45])

# min_heap.insert(12)
# print(min_heap.heap)

# # mn = min_heap.extractMin()
# # print(mn)
# # print(min_heap.heap)

# # mn1 = min_heap.extractMin()
# # print(mn1)

# # print(min_heap.heap)

# min_heap.delete1(3)
# print(min_heap.heap)
################################################################################################################################
## Heap Sort:
def heapSort(nums):
    ## heap sort algo: follows two steps
        ## 1. Build a max Heap
        ## 2. Repeatedly swap root with last node, reduce heap size by 1 and heapify
    
    def maxHeapify(nums, n, i):
        left = (2*i) + 1
        right = (2*i) + 2
        largest = i
        
        if (left < n) and (nums[left] > nums[largest]):
            largest = left
        
        if (right < n) and (nums[right] > nums[largest]):
            largest = right
        
        if largest != i:
            ## swap
            nums[i], nums[largest] = nums[largest], nums[i]
            maxHeapify(nums, n, largest)
        
        return
    
    ## build max heap
    def buildHeap(nums, n):
        last_index = n-1
        
        indx = (last_index - 1) // 2
        
        for i in range(indx, -1, -1):
            maxHeapify(nums, n, i)
        
        return
    
    ## get the size of the given array
    n = len(nums)
    
    ## step-1. build the heap
    buildHeap(nums, n)
    
    ## step-2.
    for i in range(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        maxHeapify(nums, i, 0)
    
    return 

nums = [1, 0, 2, 9, 4, 7, 11, 3, 9, 5]
heapSort(nums)
print(nums)