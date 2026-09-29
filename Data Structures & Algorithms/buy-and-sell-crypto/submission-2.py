class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        op =0
        m = prices.index(min(prices))
        for i in range(m,len(prices)):
            for j in range(i+1,len(prices)):
                # print(prices[i] , prices[j] , prices[j]-prices[i])
                op=max(op,prices[j]-prices[i])

        return op
        