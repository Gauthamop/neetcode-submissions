class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing = ascending order
        #ill just create two pointers left , right , right will start one ahead , always index1<index2 (left<right at all times)
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []



        
        