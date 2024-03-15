class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()  # Sort the costs of ice creams in ascending order
        n = len(costs)  # Get the number of ice creams available
        res = 0  # Initialize the result counter for the number of ice creams bought
        
        # Iterate through the sorted ice cream costs
        for i in range(n):
            if (coins - costs[i]) >= 0:  # If there are enough coins to buy the current ice cream
                coins -= costs[i]  # Deduct the cost of the ice cream from the available coins
                res += 1  # Increment the counter for the number of ice creams bought
        
        return res  # Return the total number of ice creams bought
