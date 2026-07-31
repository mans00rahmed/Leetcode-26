class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = min(prices[0], prices[1]) if len(prices) >= 2 else None
    
        maximum_profit = 0
        slow = 0

        for fast in range(1,len(prices)):
            if prices[slow]>prices[fast]:
                if minimum_price>=prices[fast]:
                    minimum_price=prices[fast]
                    slow=fast
                    
            else:
                current_profit=prices[fast]-prices[slow]
                if current_profit>maximum_profit:
                    maximum_profit=current_profit
                
            
        return(maximum_profit)

        