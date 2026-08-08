class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1 #non-decreasing order is ascending order
        while left<right: #but the index cannot be equal to each other
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1

            else:
                return [left+1,right+1]  #since it is a 1-indexed array


        








    
        