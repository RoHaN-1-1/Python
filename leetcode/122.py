class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        for i in range(0,len(prices)-1,1):
            if prices[i] < prices[i+1]:
                buy = prices[i]
                sell += prices[i+1] - buy
        return sell