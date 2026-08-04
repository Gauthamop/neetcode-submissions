class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={} #creating an hashmap 
        for number in nums:
            if number not in hashmap:
                hashmap[number]=1
            elif number in hashmap:
                hashmap[number]+=1
                return True

        return False
        