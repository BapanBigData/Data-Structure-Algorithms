def print_msg():
    print('hello, world!')
    print_msg1()
    return

def print_msg1():
    print('hello, world!')
    print_msg2()
    return

def print_msg2():
    print('hello, world!')
    print_msg3()
    return

def print_msg3():
    print('hello, world!')
    print_msg4()
    return

def print_msg4():
    print('hello, world!')
    return

# print_msg()
## -----------------------------------------------------------------------------
def print_num(n: int):
    print(n, end= ' ')
    print_num1(n+1)
    return

def print_num1(n: int):
    print(n, end= ' ')
    print_num2(n+1)
    return

def print_num2(n: int):
    print(n, end= ' ')
    print_num3(n+1)
    return

def print_num3(n: int):
    print(n, end= ' ')
    print_num4(n+1)
    return

def print_num4(n: int):
    print(n, end= ' ')
    return

# print_num(1)
## -----------------------------------------------------------------------------------------------
def print_nums(n: int):
    ## base case
    if n < 1:
        return
    
    print_nums(n-1)
    print(n, end=' ')
    return

# print_nums(5)

## fibobacci number
def fib(n):
    ## base case
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)

# print(fib(21))

## Binary search

def binary_search(nums, x):
    
    def solver(s, e):
        ## base case
        if s > e:
            return -1
        
        mid = (s + e) // 2
        
        if nums[mid] == x:
            return mid
        
        if nums[mid] > x:
            return solver(s, mid-1)
        else:
            return solver(mid+1, e)
        
    s = 0
    e = len(nums)-1
    
    return solver(s, e)

    
nums = [2, 3, 6, 7, 9, 11, 12]; x = 3
print(binary_search(nums, x))