from queue import PriorityQueue
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Create a dictionary to store the frequency of each word
        freq_map = {}
        for word in words:
            if word not in freq_map:
                freq_map[word] = 1
            else:
                freq_map[word] += 1
        # Step 2: Create a min-heap to maintain words sorted by frequency
        pq = PriorityQueue()
        for key in freq_map:
            pq.put([-freq_map[key], key])
        # Step 3: Retrieve the top k frequent words
        result = []
        while k > 0 and not pq.empty():
            k -= 1
            freq, element = pq.get()
            result.append(element)
        
        # Step 4: Return the list of top k frequent words
        return result

# Example usage:
# You can create an instance of the Solution class and call the topKFrequent method with the input values.
solution = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 2
result = solution.topKFrequent(words, k)
print(result)
