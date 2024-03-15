from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # Get the length of the input temperature list
        n = len(temp)
        
        # Initialize a list to store the result, initialized with zeros
        result = [0] * n
        
        # Initialize a stack to keep track of temperatures and their indices
        stack = deque()
        
        # Iterate through the temperatures
        for i in range(n):
            # While the stack is not empty and the current temperature is higher than the temperature at the top of the stack
            while stack and stack[-1][0] < temp[i]:
                # Pop the top element from the stack
                val, ind = stack.pop()
                
                # Update the result for the popped temperature's index
                result[ind] = i - ind
            
            # Push the current temperature and its index onto the stack
            stack.append([temp[i], i])
        
        # Return the final result
        return result
