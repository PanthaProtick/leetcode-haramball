class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        u=0
        d=size-1
        while u<d:
            matrix[u],matrix[d]=matrix[d],matrix[u]
            u+=1
            d-=1
        for i in range(size):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        