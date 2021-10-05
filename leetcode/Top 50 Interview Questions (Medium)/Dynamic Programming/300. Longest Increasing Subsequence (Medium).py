class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #go through finding sequences and store in dictionary
        #if you start with a certain number you have to end in a certain sqeuence
        #because you go in order
        #store in dict and return
        #implmeent find seq first then dictionary 
        
        res = 0
        
        tot = [1] * len(nums) # I had most of it down except this part, where this allows
        #you to iterate over the array without taking into account the ones that you
        #want to remove 
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tot[i] = max(tot[i], tot[j] + 1)
        
        return max(tot)



'''
optimal nlogn approach i found 

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        subs = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i] > subs[-1]: subs.append(arr[i])
            else:
                subs[bisect_left(subs, arr[i], 0, len(subs))] = arr[i]
        return len(subs)

'''