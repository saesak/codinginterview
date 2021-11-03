'''
REVISIT

FOR SOME REASON MEMOIZED VERSION FROM SOLUTION DOESN'T WORK
'''

'''
runs out of time even though i just translated it from java
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        i, j, k = 0, 0, 0
        
        memo = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
                
        def recurse(s1, s2, s3, i, j, k, memo):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            #print(i,j)
            if memo[i][j] >= 0:
                if memo[i][j] == 1:
                    return True
                else:
                    False
            
            ans = False
            
            if s3[k] == s1[i] and recurse(s1, s2, s3, i+1, j, k+1, memo):
                ans = True
            if s3[k] == s2[j] and recurse(s1, s2, s3, i, j+1, k+1, memo):
                ans = True
            
            if ans:
                memo[i][j] = 1
            else:
                memo[i][j] = 0
                                          
            return ans
        
        if (len(s1) + len(s2)) != len(s3):
            return False
        
        return recurse(s1, s2, s3, i, j, k, memo)


'''
answer that works taken from

https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS. 
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]
        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                   (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]