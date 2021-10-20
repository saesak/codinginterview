#assume nums is list of elements
#binary search assumes list is sorted, we will assume it is sorted in ascending order
#k is wanted number
#-1 in case of none existing
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, k):
            mini = 0
            maxi = len(nums) - 1 

            while mini <= maxi:
                mid = mini + (maxi - mini) // 2 
                if nums[mid] == k:
                    return mid
                if k > nums[mid]:
                    mini = mid + 1 
                if k < nums[mid]:
                    maxi = mid - 1 

            return -1
        
        return binary_search(nums, target)