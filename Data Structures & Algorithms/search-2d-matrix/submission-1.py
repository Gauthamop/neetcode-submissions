class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #m and n
        #i will loop through the different rows and j will loop through the different columns

        for i in range(len(matrix)):  #goes through the row
            left=0
            right=len(matrix[i])-1  #checks the first row
            while left<=right:
                middle=(left+right)//2
                if matrix[i][middle]==target:
                    return True
                elif matrix[i][middle]>target:
                    right=middle-1
                elif matrix[i][right]<target:
                    break      #its in the 2nd row , go checkthere
                else:
                    left=middle+1


        return False







        

        