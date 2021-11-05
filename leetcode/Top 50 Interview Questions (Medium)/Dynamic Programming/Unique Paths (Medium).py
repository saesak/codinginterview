'''
recursion solution, times out  
for long values 
'''

'''
revisit
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def recurse(m,n):
            if m < 0 or n < 0:
                return 0
            elif m == 0 and n == 0:
                return 1
            else:
                return recurse(m-1,n) + recurse(m, n-1)
            
        
        return recurse(m-1,n-1)


'''
memoization

beats 49%
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        paths = [[0 for _ in range(n)] for _ in range(m)]
        
        
        def recurse(m,n):
            if m < 0 or n < 0:
                return 0
            elif m == 0 and n == 0:
                return 1
            elif paths[m][n] > 0:
                return paths[m][n]
            else:
                paths[m][n] = recurse(m-1,n) + recurse(m, n-1)
                return paths[m][n]
        
        return recurse(m-1,n-1)

'''
good links to refer to 
java version, easier to understand logic imo
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/182143/Recursive-memoization-and-dynamic-programming-solutions


python version
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).

'''

'''
this also works
more mathy version
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        paths = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
                
        return paths[m-1][n-1]

'''
best solution is realizing that this can be solved through permutation and just using the permutation
formula 

permutation link:
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/22958/Math-solution-O(1)-space

'''