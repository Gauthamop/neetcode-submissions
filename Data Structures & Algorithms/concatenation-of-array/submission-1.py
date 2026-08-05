class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[] #created a new answer array

        for i in range(2):  #loops two times 0,1 =2
            for num in nums:
                ans.append(num)

        return ans
        