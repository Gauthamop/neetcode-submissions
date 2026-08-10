class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0 #starts at the start of the array
        right=len(numbers)-1 #starts at the end

        while left<right: #as mentioned they cannot be equal to each other
            if numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1

            else:
                return [left+1,right+1]
        


        








    
        