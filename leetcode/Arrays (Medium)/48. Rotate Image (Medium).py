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