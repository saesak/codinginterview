class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            tmp = target - nums[i]
            if tmp in nums:
                if nums.index(tmp) != i:
                    return [i, nums.index(tmp)]