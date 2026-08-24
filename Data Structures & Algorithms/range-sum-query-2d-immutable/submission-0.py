import numpy as np
class NumMatrix:
    

    def __init__(self, matrix: List[List[int]]):
        self.matrix=np.array(matrix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix=self.matrix[row1:row2+1,col1:col2+1]
        return np.sum(matrix)

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)