'''
algorithmic

o(n) time

REVISIT

had to look at the answer

indexing kinda tricky
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        counter = 1
        
        for i in range((n+1) // 2):
            
            #right
            for r in range(i, n - i):
                mat[i][r] = counter
                counter += 1
            #down
            for d in range(i+1, n - i):
                mat[d][n-i-1] = counter
                counter += 1
            #left
            for l in range(n-i-2, i-1, -1):
                mat[n-i-1][l] = counter
                counter += 1
            #up
            for u in range(n-i-2, i, -1):
                mat[u][i] = counter
                counter += 1
                
        
        return mat