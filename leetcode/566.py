class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        x = np.shape(mat)
        if r * c != x[0]*x[1]:
            return mat
        mat = np.array(mat)
        mat = mat.flatten()
        mat = mat.reshape(r,(x[0]*x[1])//r)
        return mat