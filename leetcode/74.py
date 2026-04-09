class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        flag = 0
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == target:
                    flag = 1
        if flag == 1:
            return True
        return False
