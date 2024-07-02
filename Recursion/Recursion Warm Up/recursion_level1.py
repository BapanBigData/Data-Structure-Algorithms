import math

## print n to 1
def func(n):
    ## base case
    if n == 0:
        return
    
    print(n, end=' ')
    func(n-1)
    return

def funcRev(n):
    ## base case
    if n == 0:
        return
    
    funcRev(n-1)
    print(n, end=' ')
    return

# func(8)
# print()
# funcRev(8)

## sum of digits in a given number
def sum_of_digits(n):
    ## base case
    if n == 0:
        return 0
    
    return (n % 10) + sum_of_digits(n//10)

def product_of_digits(n):
    ## base case
    if (n % 10) == n:
        return n
    
    return (n % 10) * product_of_digits(n//10)

# n = 1235
# print(sum_of_digits(n)) 
# print(product_of_digits(n))

## Reverse a number
def reverse_num(n):
    ans = [0]
    def solver(n):
        ## base case
        if n == 0:
            return 
        
        rem = n % 10
        ans[0] = (ans[0]*10) + rem
        
        solver(n//10)
        return
    
    solver(n)
    
    return ans[0]


def reverse_num1(n):
    
    def solver(n, p):
        ## base case
        if n % 10 == n:
            return n
        
        return (n % 10) * (10 ** p) + solver(n//10, p-1)
    
    ## to get number of digits in a number
    p = int(math.log10(n)) + 1
    
    return solver(n, p-1)

# num = 1001
# print(reverse_num1(num))

## number of zeros in a number
def count_zeros(n):
    ## base case
    if n % 10 == n:
        return 0
    
    if n % 10 == 0:
        return 1 + count_zeros(n // 10)
    else:
        return 0 + count_zeros(n // 10)
    

def count_zeros1(n):
    
    def solver(n, cnt):
        ## base case
        if n == 0:
            return cnt
        
        if n % 10 == 0:
            return solver(n // 10, cnt+1)
        else:
            return solver(n // 10, cnt)
    
    return solver(n, 0)

# n = 302010300
# print(count_zeros1(n))

## 1342. Number of Steps to Reduce a Number to Zero
def numberOfSteps(num):
    
    def solver(num, steps):
        ## base case
        if num == 0:
            return steps
        
        if num % 2 == 0:
            return solver(num // 2, steps+1)
        else:
            return solver(num-1, steps+1)
    
    return solver(num, 0)

print(numberOfSteps(123654))