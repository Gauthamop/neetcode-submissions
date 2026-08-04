class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0 #starting pointer , that starts at index 0 
        right=len(heights)-1
        currentarea=0
        while left<right: #never take the same height 
            calcarea=(min(heights[left],heights[right]))*abs(right-left)
            if calcarea>currentarea:
                currentarea=calcarea
            if heights[right]<heights[left]:
                right-=1
            else:
                left+=1

        
        return currentarea


        
        