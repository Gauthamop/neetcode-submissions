class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0 # starts at the middle 
        right=len(heights)-1 #one starts at the end
        maxproduct=0
        maxwater=0
        while left<right:  #dont take the same one
            maxproduct=(right-left)*min(heights[left],heights[right])
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            
            maxwater=max(maxwater,maxproduct)
        
        return maxwater

            