## Backtracking
## Given n, print all n digit numbers formed by 1, 2 in increasing order of number
def printNumbers(n: int):
    
    def solver(n, num):
        ## base case
        if n == 0:
            print(num)
            return
        
        solver(n-1, num + [1])
        solver(n-1, num + [2])
        
        return
    
    return solver(n, [])

n = 3
printNumbers(n)