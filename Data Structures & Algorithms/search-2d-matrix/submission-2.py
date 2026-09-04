class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i=0
        m=len(matrix)
        n=len(matrix[0])
        r=m*n-1

        while i<=r:

            mid=(i+r)//2
            row=mid // n
            col=mid % n
            

            if matrix[row][col]==target:
                return True
            elif matrix[row][col] > target:
                r=mid-1
            else:
                i=mid+1
        return False


        