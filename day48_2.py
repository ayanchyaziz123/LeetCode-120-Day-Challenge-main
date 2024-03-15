class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])

            # Explore all possible subsets by appending elements one by one
            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate subsets
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])    # Include the current element in the subset
                backtrack(i + 1, path)  # Recur with the next index to explore the remaining elements
                path.pop()              # Backtrack by removing the last added element

        nums.sort()  # Sort the input array to handle duplicates
        result = []  # Initialize the result list to store all subsets
        backtrack(0, [])  # Start the backtracking process with an empty path
        return result  # Return the final list of subsets
