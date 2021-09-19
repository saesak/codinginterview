# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    
    def half(self, start, end, bad_list):
        middle = int(round((start + end) / 2))
        if end < start and isBadVersion(start + 1):
            bad_list.append(start + 1)
            return start + 1
        if end < start and ~isBadVersion(start + 1):
            bad_list.append(start + 2)
            return start + 1
        if isBadVersion(middle + 1):
            return self.half(start, middle - 1, bad_list)
        if ~isBadVersion(middle + 1):
            return self.half(middle + 1, end, bad_list)
        return bad_list
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #length = len(num_list)
        start = 0 
        bad_list = []
        self.half(start, n - 1, bad_list)
        return min(bad_list)
'''
https://leetcode.com/problems/first-bad-version/
'''