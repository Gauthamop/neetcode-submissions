class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #non-decreasing order : ascending order
        left=0
        for right in range(1,len(nums)):
             #right will be one step ahead of left in this case
            if nums[right]!=nums[left]:
                left+=1 #thats means, thats the duplicate of that number should recide in the left index
                nums[left]=nums[right]
        
        return left+1
        
        