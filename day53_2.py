from typing import List

class Solution:
        
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to their corresponding letters
        digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # List to store the final combinations
        result = []

        # Backtracking function to generate combinations
        def backtrack(index, current_combination):
            # If the combination has reached the desired length, add it to the result
            if len(current_combination) == len(digits):
                result.append(current_combination)
                return

            # Iterate over the letters corresponding to the current digit
            for char in digit_to_letters[digits[index]]:
                # Recursive call with updated index and combination
                backtrack(index + 1, current_combination + char)

        # Check if the input digits string is not empty
        if digits:
            # Start the backtracking with initial index and an empty combination
            backtrack(0, "")

        # Return the final list of combinations
        return result
