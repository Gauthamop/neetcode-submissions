class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)

        for num in nums:
                hashmap[num]+=1    #increasing the count+1 in every occurence


        max_key=max(hashmap,key=hashmap.get)
            
        return max_key