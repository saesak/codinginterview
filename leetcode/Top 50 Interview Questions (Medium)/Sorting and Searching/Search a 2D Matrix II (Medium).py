'''
nlogn solution

beat 55% timewise,
35% memorywise

'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(nums, target):
            r = len(nums) - 1
            l = 0
            
            while l <= r:
                m = (r+l) // 2
                
                if nums[m] == target:
                    return True
                if nums[m] > target:
                    r = m-1
                if nums[m] < target:
                    l = m+1
            return False
        
        val = False
        
        for row in matrix:
            val = binary(row, target) or val
        
        return val

'''
dfs kinda solution

O(m+n) maximum time solution
range
goes from top right to whatever you need

beat 79% timewise
beat 35% memorywise
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        r, c = 0, n-1
        
        while r < m and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
        
        return False