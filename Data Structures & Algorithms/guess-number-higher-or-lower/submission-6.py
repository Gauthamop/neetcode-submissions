# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #dont need to create an array , just a pointer , the person who is picking the number holds the array withhimself
        left=0
        right=n-1 #n which is the length of the array is already given

        while left<=right:
            middle=left+(right-left)//2
            chosen=guess(middle)

            if chosen==-1:  #my guess is higher than the target
                right=middle-1
            elif chosen==1: #my guess is lower than the target so check rightside
                left=middle+1
            
            else:
                return middle


        return n


        

        