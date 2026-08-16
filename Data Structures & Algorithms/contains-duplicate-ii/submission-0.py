class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #given an array of nums and integer k  , return true if there are twi distinct indices , i and j in the arrray such that nums[i]==nums[j] and abs(i-j)<=k , othertwise return false

        n=len(nums)  #length of the array
        left=0
        hashset=set()
        for right in range(k): #first k elements
            if nums[right] in hashset:
                return True
            else:
                hashset.add(nums[right])  #this will add the element into the hashset

        for right in range(k,n): #the remainig elements
            if nums[right] in hashset:
                return True
            
            else:
                hashset.add(nums[right])
                hashset.remove(nums[right-k])

        return False