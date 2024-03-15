class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Initialize a frequency array to store the occurrences of each number
        freq = [0] * 501  # Assuming the maximum value of any number is 500
        
        # Count the occurrences of each number in the input array
        for val in arr:
            freq[val] += 1
        
        # Initialize the result variable to store the lucky number
        res = -1
        
        # Iterate through the input array again
        for val in arr:
            # Check if the frequency of the current number is equal to the number itself
            if freq[val] == val:
                # Update the result to the maximum of the current result and the current number
                res = max(res, val)
        
        # Return the result (which is the lucky number)
        return res
