from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # List to store the final combinations

        def backtrack(ind, current_combination):
            """
            Backtracking function to explore all combinations.

            Args:
            - ind: Index to start considering numbers from in the range [1, n]
            - current_combination: The current combination being formed
            """
            if len(current_combination) == k:
                # If the combination size is k, add it to the result list
                res.append(current_combination.copy())
                return

            for i in range(ind, n + 1):
                # Explore combinations by considering each number from 'ind' to 'n'
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()

        # Start the backtracking process with initial values
        backtrack(1, [])

        return res
