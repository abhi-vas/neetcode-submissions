class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        import numpy as np
        np_board=np.array(board)
        
        # print(np_board.shape[0])
        # print(np_board)
        for i in range(np_board.shape[0]):
            x=np_board[:,i]
            y=np_board[i,:]
            x=x[x!='.']
            # print(x)
            y=y[y!='.']
            print(y)
            if len(x)!=len(set(x)):
                return False
            if len(y)!=len(set(y)):
                return False
         
        for i in range(9):
            row=i//3
            col=i%3
            row=row*3
            col=col*3
            matrix=np_board[row:row+3,col:col+3]
            matrix=matrix[matrix!='.']
            print('hi')
            print(matrix)
            if len(matrix)!=len(set(matrix)):
                return False
        return True
    

        
        