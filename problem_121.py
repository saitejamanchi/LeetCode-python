"""
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Solution: We iterate over the price of the stock and keep track of the minimum value of the stock and the maxium profit that we have seen so far.

Time Complexity: O(n) as we iterate over the stock price on each day.

Space Complexity: O(1) as we're not creating any additional data structures. 
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitSoFar = 0
        minSoFar = prices[0]
        for i in prices[1:]:
            if i < minSoFar:
                minSoFar = i
            if (i - minSoFar) > maxProfitSoFar:
                maxProfitSoFar = (i - minSoFar)
            print(i, minSoFar, maxProfitSoFar)
        return maxProfitSoFar