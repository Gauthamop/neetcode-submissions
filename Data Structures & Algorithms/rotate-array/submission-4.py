class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n   #so for roations whose remainder is 0 for the length of the array we will perform 0 rotations

        while k:
            temp=nums[-1]  #stores the last element 
            for i in range(n-1,0,-1):
                nums[i]=nums[i-1]
            
            nums[0]=temp
            k-=1 #decrease the count of k 



