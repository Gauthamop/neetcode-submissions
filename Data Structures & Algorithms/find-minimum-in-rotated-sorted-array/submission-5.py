class Solution:
    def findMin(self, nums: List[int]) -> int:
        #to find the minimum value in a rotated sorted array 
        left=0
        right=len(nums)-1
        #lets assume the current smallest number is the first element in the array itself   

        res=nums[0]   #the first element
        
        while left<=right:
            if nums[left]<=nums[right]: #this means fromt he left most element to the right most element the array appears to be sorted if this is the case
                res=min(res,nums[left]) #this the smallest element
                break

            middle=left+(right-left)//2
            res=min(res,nums[middle])
            if nums[middle]>=nums[left]:
                left=middle+1
            else:
                right=middle-1


        return res




        