class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using floyd's cycle detection

        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]] #both start off at the same place
            if slow==fast:
                break

        
        slow2=0 #a new slow pointer
        #Phase 2 , incremeent slow1 and slow2 untill they intersect
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow


        





            

        