## recap -> Recursion

# def go_home(x, Home):
#     ## reached home
#     if x == Home:
#         print("Reached home!")
#         return
#     x += 1
#     go_home(x, Home)
#     return

# x = 1
# Home = 10
# go_home(x, Home)

def climbing_ladder(n: int):
    ## base case
    if n < 0:
        return 0
    
    if n == 0 or n == 1:
        return 1
    
    return climbing_ladder(n-1) + climbing_ladder(n-2) + climbing_ladder(n-3)

# n = 16
# print(climbing_ladder(n))



flag = False

def is_subset_sum_solver(nums, k, i, n):
    global flag  # Reference the global flag variable
    if i == n:
        if k == 0:
            flag = True
        return 
    
    is_subset_sum_solver(nums, k-nums[i], i+1, n)
    is_subset_sum_solver(nums, k, i+1, n)
    
    return 

def is_subsets_sum(nums: list, k: int) -> bool:
    # global flag   ## global flag => is optinal here because, if any flag variable isn't assign inside this fn scope
                    ## so, automatically it will take the flag variable assigned the outside of this fn scope for 
                    ## it's reference        
    n = len(nums)
    is_subset_sum_solver(nums, k, 0, n)
    
    return flag

# ChatGPT's response (below for global and local variable scope) -> 

# Yes, everything is correct in the code and the explanation.

# Your code is working correctly, and the explanation provided earlier is accurate. In the is_subsets_sum function, 
# the global flag statement is optional since there is no local variable named flag in that function's scope. 
# If there were a local variable named flag, using global flag would be necessary to explicitly reference the 
# global flag variable.

# Since there is no local variable named flag in the is_subsets_sum function, Python will automatically refer 
# to the global variable flag when you assign or modify it inside the is_subset_sum_solver function. 
# This is why the code works as intended and correctly updates the global flag variable.

# nums = [10, 12, 6, 19, 14, 20]
# k = 16
# print(is_subsets_sum(nums, k))   


def is_subset_solver(nums, k, i, n):
    if i == n:
        return k == 0
    
    inc = is_subset_solver(nums, k-nums[i], i+1, n)
    exc = is_subset_solver(nums, k, i+1, n)
    
    return True if inc else exc

def is_subset(nums, k):
    n = len(nums)
    return is_subset_solver(nums, k, 0, n)


# nums = [10, 12, 0, 19, 14, 20]
# k = 16
# print(is_subset(nums, k))   


## -------------------------------------------------------------------------------------------------------------------
cnt = 0

def cnt_subset_sum_solver(nums, k, i, n):
    global cnt
    
    if i == n:
        if k == 0:
            cnt += 1
        return
    
    cnt_subset_sum_solver(nums, k-nums[i], i+1, n)
    cnt_subset_sum_solver(nums, k, i+1, n)
    
    return

def count_subsets_sum(nums: list, k: int) -> int:
    n = len(nums)
    cnt_subset_sum_solver(nums, k, 0, n)
    
    return cnt  


def count_subsets_solver(nums, k, i, n):
    if i == n:
        if k == 0:
            return 1
        return 0
    
    inc = count_subsets_solver(nums, k-nums[i], i+1, n)
    exc = count_subsets_solver(nums, k, i+1, n)
    
    return inc + exc

def count_sunsets(nums: list, k: int) -> int:
    n = len(nums)
    return count_subsets_solver(nums, k, 0, n)

# nums = [10, 12, 6, 19, 14, 20]
# k = 16

# nums = [1, 3, 4, 0, -1, 5]; k = 4
# print(count_sunsets(nums, k))

## -------------------------------------------------------------------------------------------------

## Generating Brackets

def generate_brackets_solver(res: str, open: int, close: int, i: int, n: int):
    if i == 2*n:
        print(res)
        return
    
    if open < n:
        # res += '('
        generate_brackets_solver(res+"(", open+1, close, i+1, n)
        # res = res[:-1]  ## removing "(" during backtracking
    
    if close < open:
        # res += ')'
        generate_brackets_solver(res+")", open, close+1, i+1, n)
        # res = res[:-1]  ## removing ")" during backtracking
    
    return

def generate_brackets(n: int) -> None:
    res = ''
    generate_brackets_solver(res, 0, 0, 0, n)
    return

# generate_brackets(3)


## smart keypad

def smart_keypad_solver(ip_string, keypad, res, i):
    if i == len(ip_string):
        print(res)
        return
    
    if ip_string[i] == '0' or ip_string[i] == '1':
        smart_keypad_solver(ip_string, keypad, res, i+1)
    
    for e in keypad[ip_string[i]]:
        smart_keypad_solver(ip_string, keypad, res+e, i+1)
    
    return

def smart_keypad(n: int):
    keypad = {
        '0': '', '1': '',
        '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
        '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
    }
    
    smart_keypad_solver(str(n), keypad, '', 0)
    return
    
# smart_keypad(122)


## permutations of a given string

def permutations_solver(lst, start, n, res):
    if start == n:
        # print(''.join(lst))
        res.append(''.join(lst[:]))
        return
    
    for i in range(start, n):
        lst[i], lst[start] = lst[start], lst[i]
        permutations_solver(lst, start+1, n, res)
        
        ## restoring the positions during backtracking
        lst[i], lst[start] = lst[start], lst[i]
    
    return      

def permutations(s: str) -> list:
    lst = list(s)
    n = len(lst)
    res = []
    permutations_solver(lst, 0, n, res)
    
    return res

s = 'abcd'
print(permutations(s))    