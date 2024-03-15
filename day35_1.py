from queue import PriorityQueue
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Initialize a PriorityQueue to store elements from the matrix
        pq = PriorityQueue()
        
        # Insert all elements from the matrix into the PriorityQueue
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                pq.put(matrix[r][c])
        
        # Continue removing elements from the PriorityQueue until reaching the kth smallest element
        while True:
            k -= 1
            val = pq.get()
            if k == 0:
                return val

# Time Complexity Explanation:
# Inserting all elements into the PriorityQueue takes O(N*M * log(N*M)), where N is the number of rows and M is the number of columns.
# Extracting the kth smallest element requires k removal operations from the PriorityQueue, each taking O(log(N*M)).
# Therefore, the overall time complexity is O(N*M * log(N*M) + k * log(N*M)).
