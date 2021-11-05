class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        while j <= n - 1:
            while i <= n + m - 1 :
                if j < n:
                    if nums2[j] <= nums1[i]:
                        nums1.insert(i, nums2[j])
                        nums1.pop()
                        j = j + 1
                if i == j + m:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    j = j + 1
                i = i + 1
        j = j + 1

'''
https://leetcode.com/problems/merge-sorted-array/
'''