class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=0
        count=0
        hashmap={0: 1}
        for i in range(len(nums)):
            prefixsum+=nums[i]
            target = prefixsum - k
            if target in hashmap:
                count += hashmap[target]
            
            if prefixsum not in hashmap:
                hashmap[prefixsum]=1
            elif prefixsum in hashmap:
                hashmap[prefixsum]+=1
        
        return count