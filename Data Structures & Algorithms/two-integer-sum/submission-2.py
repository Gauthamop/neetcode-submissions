class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two sum question , here a+b=c so index i(a) j(b) and if c is also in the array , then return i and j index in an array

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                #else part when i!=j
                if nums[i]+nums[j]==target:
                    return [i,j]


        