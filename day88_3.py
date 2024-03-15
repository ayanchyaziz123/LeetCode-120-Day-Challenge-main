class Solution:
    def pivotInteger(self, n: int) -> int:
        # Calculate the prefix sum from 1 to n
        prefix_sum = 0
        
        # Base case: if n is 1, return 1 since it's the only possible pivot
        if n == 1:
            return 1
        
        # Calculate the prefix sum from 1 to n
        for i in range(1, n + 1):
            prefix_sum += i
        
        # Initialize the current sum
        curr = 0
        
        # Iterate from n to 1 to find the pivot integer
        while n != 0:
            # Update the current sum by adding the current value of n
            curr += n
            
            # Check if the current sum is equal to the prefix sum
            if curr == prefix_sum:
                # If so, n is the pivot integer, so return it
                return n
            
            # Update the prefix sum by subtracting the current value of n
            prefix_sum -= n
            
            # Decrement n for the next iteration
            n -= 1
        
        # If no pivot integer is found, return -1
        return -1
