class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #search insert position 
        #given already an sorted array 
        #given target value , if found return the index , if not  , return the index where it would be if it were inserted in order

        #array is already sorted in this case
        left=0
        right=len(nums)-1
        while left<=right:  #can be equal but never cross
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle #done base case , if u find the number return it

            elif nums[middle]>target: #its on the left side
                right=middle-1
            elif nums[middle]<target: #its on the right side
                left=middle+1

        return right+1



        #at the end anyways we will get both the indexes which pertain closes to the number 


        