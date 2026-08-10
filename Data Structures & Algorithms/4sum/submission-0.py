class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #fourSum problem 
        #again unique quadruplets

        #again
        nums.sort()
        ans=set()
        #so we create a set , or a hashset as it doesnt allow duplicate values

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for z in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[z]==target:
                            ans.add((nums[i],nums[j],nums[k],nums[z]))

        return list(ans)







        