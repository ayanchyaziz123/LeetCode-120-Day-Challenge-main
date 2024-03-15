from collections import Counter
from typing import List

class Solution:
    def countCompleteSubarrays(self, A: List[int]) -> int:
        # Get the length of the array A
        n = len(A)
        # Get the number of unique elements in A
        k = len(set(A))
        # Initialize the result variable
        res = i = 0
        # Create a Counter to keep track of the frequency of elements
        freq = Counter()
        
        # Iterate through the array A
        for j in range(n):
            # Update the frequency of the current element
            freq[A[j]] += 1
            # Check if all unique elements have been seen
            while len(freq) == k:
                # Update the frequency of the element at index i
                freq[A[i]] -= 1
                # If the frequency becomes 0, remove the element from the Counter
                if freq[A[i]] == 0:
                    del freq[A[i]]
                # Move the left pointer (i) to the next index
                i += 1
            # Update the result by adding the index i
            res += i
        # Return the result
        return res
