from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(start, target, store):
            # Base case: if target becomes negative, return
            if target < 0:
                return
            
            # If we reach the target sum, add the current combination to the result
            if target == 0:
                res.append(store.copy())
                return
            
            # Explore all candidates starting from the current index
            for i in range(start, len(candidates)):
                # Choose the current candidate
                store.append(candidates[i])
                
                # Recursive call with updated target and index
                dfs(i, target - candidates[i], store)
                
                # Backtrack: remove the last added candidate to explore other possibilities
                store.pop()
        
        # Start the DFS from the beginning of the candidates list
        dfs(0, target, [])
        return res
