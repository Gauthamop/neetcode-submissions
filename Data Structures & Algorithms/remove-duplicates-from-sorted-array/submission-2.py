class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #non-decreasing order ---> ascending order
        left=0   #starting at the first element
        right=0 
        n=len(nums)
        result=[]
        while right<n:
            nums[left]=nums[right]
            while right<n and nums[right]==nums[left]: #till its equal , there are still duplicates and u put that element to L again
                right+=1  #when its not equal then the duplicates are over and now shift the position of left , 1 incerase
            left+=1
        return left          

        
        


        