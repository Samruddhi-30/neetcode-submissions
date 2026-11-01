class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])

        for mat in matrix:
            if mat[n-1]>=target:
                if target in mat:
                    return True

        return False
        