# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def binary(n):            
            l = 1
            r = n 
            
            while l <= r:
                mid = (l+r) // 2
                
                if isBadVersion(mid):
                    r = mid -1
                else:
                    l = mid + 1 
            
            return l
        
        return binary(n)

'''
REVISIT

why do i return l instead of r 

and why do I set l<=r when doing binary search??
'''