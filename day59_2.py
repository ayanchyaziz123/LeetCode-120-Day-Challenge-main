from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        x = 0  # Initialize variable to represent the index based on the ruleKey
        if ruleKey == "color":  # Check if the ruleKey is "color"
            x = 1  # If "color", set the index to 1 (since "color" corresponds to the second element in each item)
        if ruleKey == "name":  # Check if the ruleKey is "name"
            x = 2  # If "name", set the index to 2 (since "name" corresponds to the third element in each item)
        res = 0  # Initialize a variable to store the count of matches
        for item in items:  # Iterate over each item in the list of items
            if item[x] == ruleValue:  # Check if the value at index x of the current item matches the ruleValue
                res += 1  # If it matches, increment the count of matches
        return res  # Return the total count of matches
