class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=0
        prefixsumarr=[]
        postfixsumarr=[]
        postfixsum=0
        
        for i in range(len(nums)):
            prefixsumarr.append(prefixsum)       #forgot to add edgecase , to the left its 0 
            prefixsum+=nums[i]

        for j in range(len(nums)-1,-1,-1):
            postfixsumarr.append(postfixsum)  #here aswell to the right its 0
            postfixsum+=nums[j]
        
        postfixsumarr.reverse()

        for i in range(len(nums)):
            if prefixsumarr[i]==postfixsumarr[i]:
                return i
        
        return -1