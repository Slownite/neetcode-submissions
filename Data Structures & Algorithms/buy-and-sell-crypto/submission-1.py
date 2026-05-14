
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      min_price = float('inf')
      maxProfit = 0
      for p in prices:
        min_price = min(min_price, p)
        maxProfit = max(maxProfit, p - min_price)
      return maxProfit
        

