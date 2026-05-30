class Solution:
    # two pointers
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     l = 0
    #     r = 1
    #     while r < len(prices):
    #         if prices[l] < prices[r]:
    #             res = max(res, prices[r]-prices[l])
    #         else:
    #             l = r
    #         r += 1
    #     return res
    
    # 1D DP
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]

        for sell in prices:
            res = max(res, sell - minBuy)
            minBuy = min(minBuy, sell)
        return res
