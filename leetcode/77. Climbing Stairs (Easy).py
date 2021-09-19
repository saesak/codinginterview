'''
https://leetcode.com/problems/climbing-stairs/
'''

class Solution(object):
    
    def helper(self, n, hashmap):
        if n == 1:
            return 1
        if n == 0:
            return 1
        if n in hashmap:
            return hashmap[n]
        
        hashmap[n] = self.helper(n-1, hashmap) + self.helper(n-2, hashmap)
        return hashmap[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashmap = dict()
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 0:
            return 0
        return self.helper(n, hashmap)
