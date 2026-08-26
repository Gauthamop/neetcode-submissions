class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #this is an floyds cycle problem where we have a slow and fast pointer 

        slow=0
        fast=0

        while True:
            slow=nums[slow]  #moves every iteration once
            fast=nums[nums[fast]] #moves every iteration twice

            if slow==fast:
                break
        

        #we start a slow2 pointer
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]

            if slow==slow2:
                return slow2



        