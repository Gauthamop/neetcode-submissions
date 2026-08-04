class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing = ascending order
        #ill just create two pointers left , right , right will start one ahead , always index1<index2 (left<right at all times)
        left,right=0,len(numbers)-1
        #make sure the array is already sorted in ascending order
        while left<right:
            currentsum=numbers[left]+numbers[right]
            if currentsum>target:
                right-=1
            elif currentsum<target:
                left+=1
            else:
                return [left+1,right+1]
        
        return []



        
        