
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l = 0
      maxPr = 0
      for r in range(len(prices)):
        if prices[r] < prices[l]:
          l = r
        else:
          maxPr = max(prices[r] - prices[l], maxPr)
      return maxPr
        

