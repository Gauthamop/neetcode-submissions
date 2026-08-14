class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #ascending order---> non-decreasing

        if target in nums:
            return True

        else:
            return False