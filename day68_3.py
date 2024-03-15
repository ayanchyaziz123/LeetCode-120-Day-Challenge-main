class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Create a dictionary to store the frequency of each number
        freq_map = {}
        
        # Iterate through the input list
        for num in nums:
            # If the number is not in the dictionary, add it with frequency 1
            # Otherwise, increment its frequency
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        # Initialize the result variable to store the sum of unique elements
        res = 0
        
        # Iterate through the dictionary
        for key in freq_map:
            # If the frequency of the number is 1, add it to the result
            if freq_map[key] == 1:
                res += key
        
        # Return the sum of unique elements
        return res
