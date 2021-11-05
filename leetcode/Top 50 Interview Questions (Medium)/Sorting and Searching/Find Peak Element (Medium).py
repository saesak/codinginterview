class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        
        while left < right: #doesn't work if you use left <= right
            mid = left + (right - left) // 2 
            
            if nums[mid] > nums[mid+1]:
                right = mid
            if nums[mid] < nums[mid+1]:
                left = mid + 1

        return left

'''
revisit???
'''