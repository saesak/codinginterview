'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

Had to look at the answer even though it was easy. I couldn't figure out how to deal
with the indexing changing until I looked at the discuss section :( thats an L
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        n = len(nums)
        i = 0
        
        if n == 0:
            return 0
        
        while i < n:
            if prev == nums[i]:
                nums.pop(i)
                n = len(nums)
                #prev = nums[i]
                i = i - 1 
            if prev != nums[i]:
                prev = nums[i]
            
            i += 1 
        
        return len(nums)