class Solution:
    def totalMoney(self, n: int) -> int:
        # Initialize variables
        day = 1  # Represents the current day of the week
        inc = 0  # Represents the incremental amount to add to each day's earnings
        res = 0  # Represents the total amount of money
        
        # Iterate over each week
        for i in range(n):
            # Add the earnings for the current day
            res += day + inc
            
            # Increment the day and check if it's a new week (if it reaches 8)
            day += 1
            if day == 8:
                inc += 1  # Increment the incremental amount for the next week
                day = 1   # Reset the day to the first day of the week
                
        return res  # Return the total amount earned
