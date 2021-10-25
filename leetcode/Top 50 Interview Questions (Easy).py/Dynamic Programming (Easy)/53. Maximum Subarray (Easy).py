class Solution:
    '''def merge(self, nums, hashmap):
        currsum = 0
        maxsum = 10e-6
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                
    
    def maxSubArray(self, nums: List[int]) -> int:
        hashmap = dict()'''
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = -10e6
        for ele in nums:
            currsum = max(currsum+ele, ele)
            if currsum > maxsum:
                maxsum = currsum
                
        return maxsum 

'''
https://leetcode.com/problems/maximum-subarray/
'''