class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        res =0

        while r<=len(prices)-1:
            if prices[l]<prices[r]:
                pro = prices[r]-prices[l]
                res=max(pro,res)
            else:
                l=r
            r+=1
        return res
            
        