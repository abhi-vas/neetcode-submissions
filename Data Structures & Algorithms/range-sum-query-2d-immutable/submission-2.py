
class NumMatrix:
    

    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix),len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if  j>0:
                    matrix[i][j]+=matrix[i][j-1]
                    
                else:
                    matrix[i][j]==matrix[i][j]
                    
        for j in range(col):
            for i in range(row):
                if i>0:
                    matrix[i][j]+=matrix[i-1][j]
                    
                else:
                    matrix[i][j]==matrix[i][j]
                    
        self.matrix=matrix
        
                
                

        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1>0 and row2>0 and col1>0 and col2>0:
            sumi=self.matrix[row2][col2]+self.matrix[row1-1][col1-1]-(self.matrix[row2][col1-1]+self.matrix[row1-1][col2])
            return sumi
        if row1==0 and col1==0:
            sumi=self.matrix[row2][col2]
            return sumi
        if row1==0:
            sumi=self.matrix[row2][col2]-(self.matrix[row2][col1-1])
            return sumi
        if col1==0:
            sumi=self.matrix[row2][col2]-(self.matrix[row1-1][col2])
            return sumi
        

        
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)