class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #basic binary search algorithm 

        left=0
        right=len(nums)-1

        while left<=right:
            #calculate them middle , based on the middle , we lessen the workspace by moving the left and right pointer respectively 
            middle=(left+right)//2 #rounding off the closest whole number
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            else:#then the element/target is on the right/half of the array
                left=middle+1

        
        return -1

                

        