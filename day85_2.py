class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Sort the prices in ascending order
        prices.sort()
        
        # Check if it's possible to buy the two cheapest chocolates
        if (money - (prices[0] + prices[1])) > -1:
            # If so, return the remaining money after buying the chocolates
            return money - (prices[0] + prices[1])
        
        # If it's not possible to buy the chocolates, return the original amount of money
        return money
