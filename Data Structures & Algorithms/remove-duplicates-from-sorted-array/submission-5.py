class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #to remove duplicates from nums in-place
        #untill a non-duplicate number appears 
        i=0 #both start from the first element in the array
        j=0 #starts from the start of the array
        n=len(nums)
        while j<n:  #do not pass n or equal to n
            nums[i]=nums[j]
            while j<n and nums[j]==nums[i]:
                j+=1  #increase

            i+=1 #when it stops being equal increase i

        return i








        