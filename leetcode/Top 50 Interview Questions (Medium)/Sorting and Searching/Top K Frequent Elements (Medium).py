
'''awful solution'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        res = []
        
        for i in range(len(nums)):
            curr = nums[i]
            
            if curr in num_dict:
                num_dict[curr] = num_dict[curr] + 1
            else:
                num_dict[curr] = 1
                
        sort_orders = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            res.append(sort_orders[i][0])
        
        return res

'''better
https://leetcode.com/problems/top-k-frequent-elements/solution/

REVISIT!!!!

'''



