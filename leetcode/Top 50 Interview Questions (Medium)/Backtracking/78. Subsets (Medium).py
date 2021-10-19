class Solution:
    def backtrack(self, nums, n, start, final, temp):
        final.append(temp[:])
        for i in range(start, n):
            temp.append(nums[i])
            self.backtrack(nums, n, i+1, final, temp)
            temp.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final = [] #accounts for [] case 
        temp = []
        self.backtrack(nums, n, 0, final, temp)
        return final

'''
kinda still in the process of getting backtracking, i looked at this guy's
solutions
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/discuss/18284/Backtrack-Summary:-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)

But getting there 

These guys don't actually really backtrack in the way that
they actually go through all possible solutions and filter
out the wrong ones. They just recurse in a smart way to get
all the ways to do it correctly, if that kind of makes sense.
What's a true backtracking solution? Haven't seen one yet.
I'd guess it's less efficient?

'''