class Solution:
    def reverse(self, x: int) -> int:
        
        
        str_list = []
        n = len(str(x))
        for i in range(n):
            str_list.insert(i, str(x)[i])
                
        str_list.reverse()
        
        if x < 0:
            str_list.insert(0, str_list.pop(-1))
                
        final = ''.join(str_list)
        
            
        final = int(final)
        
                
        if final < -2**(31) or final > (2**(31) - 1):
            return 0
        
        return final

'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

'''

#if you actually need to reverse a string, you can do this one liner 
#stringname[stringlength::-1] # method 1 