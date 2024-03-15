from queue import PriorityQueue

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Create a hash map to store the frequency of each character
        freq_map = {}
        for i in range(len(s)):
            if s[i] not in freq_map:
                freq_map[s[i]] = 1
            else:
                freq_map[s[i]] += 1
        # Step 2: Create a min-heap to maintain characters sorted by frequency
        pq = PriorityQueue()        
        for key in freq_map:
            pq.put([-freq_map[key], key])
        
        # Step 3: Build the result string by appending characters based on their frequency
        result = ""
        while not pq.empty():
            freq, element = pq.get()
            # Append the character to the result string for each occurrence
            for i in range(-freq):
                result += element
        # Step 4: Return the final result string
        return result

# Example usage:
# You can create an instance of the Solution class and call the frequencySort method with the input string.
solution = Solution()
input_str = "tree"
result = solution.frequencySort(input_str)
print(result)
