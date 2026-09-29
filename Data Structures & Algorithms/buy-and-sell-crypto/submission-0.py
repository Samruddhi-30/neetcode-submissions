class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)==1:
            return 0
        op =[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                # print(prices[i] , prices[j] , prices[j]-prices[i])
                op.append(prices[j]-prices[i])

        if max(op)<0 :
            return 0
        return max(op)
        