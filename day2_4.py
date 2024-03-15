from collections import defaultdict
import sys

#Leetcode problem:-> 169. Majority Element
#Ayan's code

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Create a dictionary to store the count of each element
        count_map: dict = defaultdict(int)

        # Count occurrences of each element in the list
        # Time complexity: O(n), where n is the length of the input list
        for i in range(len(nums)):
            count_map[nums[i]] += 1

        # Initialize variables to keep track of the maximum occurrence and the majority element
        max_occurrence: int = -1
        majority_element: int = 0

        # Iterate through the dictionary to find the majority element
        # Time complexity: O(n), where n is the number of unique elements in the list
        for key in count_map:
            if count_map[key] > max_occurrence:
                max_occurrence = max(count_map[key], max_occurrence)
                majority_element = key

        return majority_element

# Example usage
nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums))
