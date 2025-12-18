# Day 2 
# Problem : Best Time To Buy And Sell Stock 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different
# day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 

# Use Pointer Left (l) , Right (r) : This Does the comparison 
# Simply 
# if price(l)<price(r) then , profit = price (r) - price (l) 
# else , left = right , right +=1 
# return profit 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l, r = 0, 1  # l is the index for buying (minimum price so far), r for selling
        maxP = 0     # Initialize maximum profit to 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r  # Update l to the current r if a lower price is found
            r += 1
        
        return maxP