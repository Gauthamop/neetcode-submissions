class Solution:
    def mySqrt(self, x: int) -> int:
        #here if x=9 , [1,2,3,4,5,6,7,8,9]
        left=0
        right=x #taking x as the last digit in the integer


        while left<=right:
            middle=left+(right-left)//2
            if middle**2==x:
                return middle

            elif middle**2>x:  #search on the left hand side
                right=middle-1
            else:
                left=middle+1


        
        if x==0:
            return 0
        else:
            return right
        