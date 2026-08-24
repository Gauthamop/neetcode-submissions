class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #normal approach using hashset 

        hashset=set()

        for num in nums:
            if num in hashset:
                return num

            else:
                hashset.add(num)


        return -1
        