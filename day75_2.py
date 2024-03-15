class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the costs in descending order
        cost.sort(reverse=True)
        
        # Get the length of the cost array
        n = len(cost)
        
        # Initialize the result variable to store the minimum cost
        res = 0
        
        # Initialize the index variable
        i = 0
        
        # Iterate through the costs array
        while i < n:
            # Add the current cost to the result
            res += cost[i]
            i += 1
            
            # Check if we have reached the end of the array
            if i >= n:
                return res
            
            # Add the next cost to the result (skipping one element)
            res += cost[i]
            i += 2
            
        # Return the result
        return res
