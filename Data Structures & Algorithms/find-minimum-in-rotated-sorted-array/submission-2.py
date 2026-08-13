class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]   #the current minimum number
        left=0
        right=len(nums)-1


        while left<=right:
            if nums[left]<nums[right]:  #already sorted in this case
                res=min(res,nums[left])
                break

            
            middle=(left+right)//2
            res=min(res,nums[middle])
            if nums[middle]>=nums[left]: #if the current middle is greater than the left element
                left=middle+1
            else:
                right=middle-1


        return res


        