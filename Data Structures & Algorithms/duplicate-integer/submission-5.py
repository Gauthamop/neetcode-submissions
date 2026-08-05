class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #to check if an array contains a duplicate valule
        #if anything repeats more that once in the array 
        #we can create an hashset put values into it , and if another values comes in which is the same ---> then its a duplicate value

        hashset=set() #created a set
        for num in nums:
            if num in hashset:
                return True #there is a duplicate value in the array

            else:
                hashset.add(num)

        return False #if none of the numbers are duplcicated till the end , return false
        