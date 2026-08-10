class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #fourSum problem 
        #again unique quadruplets
        #we take 2 numbers that do not repeat and have a left and right pointer that will keep track of the other two numbers
        nums.sort()
        res=[]
        for i in range(len(nums)):# goes through the entire array
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)):  #next starting element , that is not i
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                left=j+1
                right=len(nums)-1
                while left<right: #cannot cross ,and cannot be equal as we need distinct index values
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:  #towards the end if its equal
                            left+=1
                        while left<right and nums[right]==nums[right+1]: #towards the end if its equal
                            right-=1
                        
                    elif total<target:
                        left+=1
                    else:
                        right-=1

        return res

            













        