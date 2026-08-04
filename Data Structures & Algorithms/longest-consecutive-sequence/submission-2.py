class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        bigarr=[]
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            sum=0
            count=0
            sum=nums[i]
            while sum in nums:
                sum=sum+1
                count+=1
            bigarr.append(count)

        return max(bigarr)


                

        