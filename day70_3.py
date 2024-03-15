from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Initialize variables
        i = 0
        n = len(details)
        res = 0
        
        # Iterate through each detail
        while i < n:
            # Check if the age indicates a senior
            if int(details[i][11]) == 6 and int(details[i][12]) >= 1:  # Age starts at index 11
                res += 1
            elif int(details[i][11]) > 6:  # If age is greater than 60
                res += 1
            
            # Move to the next detail
            i += 1
        
        # Return the count of seniors
        return res
