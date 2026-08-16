class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #minimum size subarray sum
        left=0 #starts
        n=len(nums)
        prefixsumarray=[0]
        sum=0
        #prefix sum calculation before hand
        minlength=float('inf')
        for num in nums:
            sum+=num
            prefixsumarray.append(sum)  #creates a prefix sum

        #prefix sum is calculated 

        for right in range(n):
            while left<=right and prefixsumarray[right+1]-prefixsumarray[left]>=target:
                window=right-left+1  #the current windowrange
                minlength=min(window,minlength)
                left+=1




        if minlength==float('inf'):
            return 0
        else:
            return minlength


        