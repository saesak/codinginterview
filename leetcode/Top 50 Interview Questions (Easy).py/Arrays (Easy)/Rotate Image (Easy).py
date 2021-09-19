'''
Math trick lets you do it in O(n^2) time if n is the length of the list
not the number of elements.

Just pay attention to the examples outputs given and find the math trick/pattern
that lets you do it easily and efficiently. Then you don't need to do it the
hard way iterating over every element in the grid.

Still a problem worth reviewing though. 

https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            tmp = []
            for j in range(n-1, -1, -1): 
                tmp.append(matrix[j][i])
            matrix.append(tmp)
            
        for i in range(n):
            matrix.pop(0)