class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #nums original array 
        ans=[]
        for i in range(2):  #since we need a length of 2
            for num in nums:
                ans.append(num)

        
        return ans


        