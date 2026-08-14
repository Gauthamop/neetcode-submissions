class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #to search for a target in a rotated sorted array
        left=0
        right=len(nums)-1

        while left<=right:
            middle=left+(right-left)//2
            if nums[middle]==target:  #if we find the elemenet in the middle , return it 
                    return middle

            if nums[left]<=nums[middle]:  #the left hand side is sorted
                if target>nums[middle] or target<nums[left]:
                    left=middle+1
                else:
                    right=middle-1

            else:
                if target<nums[middle] or target>nums[right]:
                    right=middle-1
                else:
                    left=middle+1


        return -1

    


            


        