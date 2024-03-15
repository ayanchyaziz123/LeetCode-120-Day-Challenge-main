class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}  # Dictionary to store the frequency of fruits
        n = len(fruits)  # Get the length of the input list
        start = 0  # Initialize the start index of the window
        have = 0  # Initialize the number of fruits in the current window
        mx = 0  # Initialize the maximum number of fruits seen so far
        
        # Iterate through the input list
        for i in range(n):
            if fruits[i] not in freq:  # If the fruit is not in the dictionary
                freq[fruits[i]] = 1  # Add it to the dictionary with frequency 1
            else:  # If the fruit is already in the dictionary
                freq[fruits[i]] += 1  # Increment its frequency
            
            have += 1  # Increment the count of fruits in the current window
            
            # Check if the number of different fruits in the current window exceeds 2
            while len(freq) > 2:
                freq[fruits[start]] -= 1  # Decrement the frequency of the fruit at start index
                if freq[fruits[start]] == 0:  # If the frequency becomes 0
                    del freq[fruits[start]]  # Remove the fruit from the dictionary
                start += 1  # Move the start index to the right
                have -= 1  # Decrease the count of fruits in the current window
            
            # Update the maximum number of fruits seen so far
            mx = max(mx, have)
        
        return mx  # Return the maximum number of fruits in a contiguous subarray
