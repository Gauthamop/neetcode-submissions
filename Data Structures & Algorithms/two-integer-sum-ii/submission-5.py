class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing = ascending order
        #ill just create two pointers left , right , right will start one ahead , always index1<index2 (left<right at all times)
        for left in range(0,len(numbers)):
            right=len(numbers)-1  #leave out the 2nd last element , as right pointer will take care of that
            while right>left:   #as long as right is greater than left
                if numbers[left]+numbers[right]==target:
                    return [left+1,right+1]
                else:
                    right-=1                #this question is taking every single pair

        




        
        