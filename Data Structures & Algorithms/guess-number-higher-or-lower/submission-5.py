# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #simple binary search , if the target conditions that come from the Pre-Defined API that is set up 
        l=0 #left pointer
        r=n-1  #already sorted array #right pointer
        while l<=r:
            middle=(l+r)//2
            taken=guess(middle)
            if taken==-1: #guess was higher than the number he picked so check left
                r=middle-1
            elif taken==1:
                l=middle+1
            else: #found the number 
                return middle

        if not (l<=r):
            return n
        

        