class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        # Prefix sum array
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        left = 0
        minlength = float("inf")

        for right in range(n):
            # Sum of nums[left ... right]
            while left <= right and prefix[right + 1] - prefix[left] >= target:
                window = right - left + 1
                minlength = min(minlength, window)  #just calculate the length whenever the prefix sum in the subarray is >=target
                left += 1

        return 0 if minlength == float("inf") else minlength