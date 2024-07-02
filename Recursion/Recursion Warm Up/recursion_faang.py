## Leetcode: 17. Letter Combinations of a Phone Number
## Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
## A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(digits: str) -> list[str]:
    if digits == '':
        return []
    
    # let's define a dict which will map digits to the corresponding letters
    mp = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz' 
    }
    
    def solver(i, ans, res):
        ## base case
        if i == len(digits):
            res.append(ans)
            return res
        
        curr = digits[i]
        for e in mp[curr]:
            solver(i+1, ans+e, res)
        
        return res
    
    return solver(0, '', [])


def numFunctionCallsPad(digits: str) -> int:
    mp = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz' 
    }
    
    def solver(i):
        cnt = 0
        ## base case
        if i == len(digits):
            return 1
        
        curr = digits[i]
        for _ in mp[curr]:
            cnt += solver(i+1)
        
        return cnt
    
    return solver(0)

# digits = '272'
# # print(letterCombinations(digits))
# print(numFunctionCallsPad(digits))
###############################################################################################################################
## Dice problem: Variation of subset with given target sum
def diceThrow(dice: list[int], k: int) -> list[list[int]]:
    
    def solver(k, ans, res):
        ## base case
        if k == 0:
            res.append(ans)
            return res
        
        for num in dice:
            if k >= num:
                solver(k-num, ans + [num], res)
        
        return res
    
    return solver(k, [], [])


def numFunctionCallsDiceThrow(dice: list[int], k: int) -> int:
    
    def solver(k):
        cnt = 0
        ## base case
        if k == 0:
            return 1
        
        for num in dice:
            if k >= num:
                cnt += solver(k-num)
        
        return cnt
    
    return solver(k)

# nums = [1, 2, 3, 4, 5, 6]
# print(diceThrow(nums, 6))
# print(numFunctionCallsDiceThrow(nums, 6))
## ---------------------------------------------------------------------------------------------------------------------------------------
## You have n  tiles, where each tile has one letter tiles[i] printed on it.
## Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
def numTilePossibilities(tiles: str) -> list[str]:
    
    def generateSubseqs(i, sub_seq, res):
        ## base case
        if i == len(tiles):
            if sub_seq:
                res.append(sub_seq)
            return res
        
        ## include curr element
        generateSubseqs(i+1, sub_seq + tiles[i], res)
        
        ## ignore the currect element
        generateSubseqs(i+1, sub_seq, res)
        
        return res
    
    def generatePermutations(s, i, perm, res):
        ## base case
        if i == len(s):
            res.append(perm)
            return res
        
        curr = s[i]
        for j in range(len(perm)+1):
            generatePermutations(s, i+1, perm[:j] + curr + perm[j:], res)
        
        return res
    
    sub_seqs = generateSubseqs(i=0, sub_seq='', res=[])
    
    result_set = set()
    for seq in sub_seqs:
        ans = generatePermutations(seq, i=0, perm='', res=[])
        
        for e in ans:
            result_set.add(e)
    
    return len(result_set)

# tiles = 'FALLOFMODI'
# print(numTilePossibilities(tiles))
##--------------------------------------------------------------------------------------------------------------------------------------
