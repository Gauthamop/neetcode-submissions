class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #best time to buy and sell stock 
        #sliding window approach
        #variable type sliding window
        left=0
        n=len(prices)
        profit=0 #current profit=0
        max_profit=0

        for right in range(left,n):
            profit=0
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit,profit)

            else:
                left=right #the next least buying price


        return max_profit
        





        