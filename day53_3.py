from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # List to store the final combinations of parentheses
        result = []

        # Backtracking function to generate combinations
        def backtrack(combination, open_count, close_count):
            # If both open and close counts are zero, the combination is valid
            if open_count == 0 and close_count == 0:
                result.append(combination)
                return
            
            # If there are remaining open parentheses, add an open parenthesis
            if open_count > 0:
                backtrack(combination + '(', open_count - 1, close_count)
            
            # If there are remaining close parentheses and more open than close
            if close_count > 0 and open_count < close_count:
                backtrack(combination + ')', open_count, close_count - 1)

        # Start the backtracking with an empty combination and initial open and close counts
        backtrack("", n, n)
        
        # Return the final list of combinations
        return result
