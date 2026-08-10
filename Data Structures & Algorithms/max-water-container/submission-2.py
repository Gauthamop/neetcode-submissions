class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer method
        left=0 #starting index
        right=len(heights)-1 #last index 
        heightcalculation=0
        maxproduct=0

        while left<right: #cannot cross , nor be equal 
            heightcalculation=(right-left)*min(heights[left],heights[right])
            if heights[left]<heights[right]:# in search of a bigger height
                left+=1
            else:
                right-=1
            
            maxproduct=max(maxproduct,heightcalculation)


        return maxproduct




        