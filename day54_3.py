from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # Sort the candidates to make skipping duplicates easier
        candidates.sort()

        def backtrack(ind, remaining_target, current_combination):
            """
            Backtracking function to explore all combinations.

            Args:
            - ind: Index to start considering candidates from in the 'candidates' list
            - remaining_target: The remaining target sum to be achieved
            - current_combination: The current combination being formed
            """
            if remaining_target < 0:
                return
            if remaining_target == 0:
                res.append(current_combination.copy())
                return

            for i in range(ind, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > ind and candidates[i] == candidates[i-1]:
                    continue

                current_combination.append(candidates[i])
                backtrack(i + 1, remaining_target - candidates[i], current_combination)
                current_combination.pop()

        # Start the backtracking process with initial values
        backtrack(0, target, [])

        return res
