from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Initialize an empty list to store the result
        res = []
        
        # Adjust the value of 'm' if 'n' is odd
        m = n
        if n % 2 != 0:
            m = n - 1
        
        # Initialize a counter 'cnt' with an arbitrary large value
        cnt = 1000
        
        # Initialize a counter 'c' to keep track of how many numbers have been added
        c = 0
        
        # Iterate 'm' times to generate positive and negative integers
        for i in range(m):
            c += 1
            
            # If 'i' is even, append 'cnt' to the result list
            if i % 2 == 0:
                res.append(cnt)
            # If 'i' is odd, append '-cnt' to the result list
            else:
                res.append(-cnt)
            
            # Reset the counter 'c' after adding two numbers
            if c == 2:
                c = 0
                cnt -= 1
        
        # If 'n' is odd, append '0' to the result list
        if n % 2 != 0:
            res.append(0)
            return res
        
        # Return the result list
        return res
