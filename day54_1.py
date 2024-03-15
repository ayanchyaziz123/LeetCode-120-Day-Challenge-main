from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []  # List to store the final combinations
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Available numbers to form combinations

        def backtrack(start, remaining_sum, current_combination):
            """
            Backtracking function to explore all combinations.

            Args:
            - start: Index to start considering numbers from in the 'numbers' list
            - remaining_sum: The remaining sum to be achieved
            - current_combination: The current combination being formed
            """
            if remaining_sum == 0 and len(current_combination) == k:
                # If the required sum is achieved and the combination has k elements,
                # add it to the result list
                res.append(current_combination.copy())
                return

            if len(current_combination) >= k or remaining_sum < 0:
                # If the combination size exceeds k or the remaining sum becomes negative,
                # stop exploring this branch of the combination
                return

            for i in range(start, len(numbers)):
                # Explore combinations by considering each number from 'start' index
                current_combination.append(numbers[i])
                backtrack(i + 1, remaining_sum - numbers[i], current_combination)
                current_combination.pop()

        # Start the backtracking process with initial values
        backtrack(0, n, [])

        return res
