from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Initialize frequency dictionaries for source and destination cities
        freq1 = {}  # For source cities
        freq2 = {}  # For destination cities
        
        # Count the frequency of each city in the paths
        for u, v in paths:
            # Update the frequency for source city 'u'
            if u not in freq1:
                freq1[u] = 1
            else:
                freq1[u] += 1
            
            # Update the frequency for destination city 'v'
            if v not in freq2:
                freq2[v] = 1
            else:
                freq2[v] += 1
        
        # Iterate through the destination cities
        for key in freq2:
            # Check if the frequency of the destination city is 1
            # and if it's not present as a source city
            if freq2[key] == 1 and key not in freq1:
                # If so, return the destination city as the answer
                return key
