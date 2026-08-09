
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Push n elements from nums2 into the empty space in nums1
        # Then sort nums1

        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()

