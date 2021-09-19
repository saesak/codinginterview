class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #return s.reverse()  python 1 liner for reversing lists

        #if you actually need to reverse a string, you can do this one liner 
        #stringname[stringlength::-1] # method 1 
        
        

        n = len(s)
        
        for i in range(n):
            val = s.pop(-1)
            s.insert(i, val)