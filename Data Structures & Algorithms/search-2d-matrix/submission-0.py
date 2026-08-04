class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,col=len(matrix),len(matrix[0])
        #number of cols and number of rows

        top,bot=0,rows-1   #bottom row
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]: #checking middle row
                top=row+1  #rows larger than this row
            elif target<matrix[row][0]:
                bot=row-1
            else: #the target is in the current row
                break
        
        if not (top<=bot):
            return False
            
            #run binary search in the current row
        row=(top+bot)//2
        l,r=0,col-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[row][m]:
                l=m+1
            elif target<matrix[row][m]:
                r=m-1
            else:
                return True
        return False
                