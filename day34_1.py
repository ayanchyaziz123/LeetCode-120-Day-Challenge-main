from typing import List
from queue import PriorityQueue

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a PriorityQueue to store elements with priority based on the k-th column
        pq = PriorityQueue()
        
        # Get the number of rows and columns in the 'score' matrix
        row_size = len(score)
        col_size = len(score[0])
        
        # Insert each row into the PriorityQueue with priority based on the value in the k-th column
        for i in range(row_size):
            pq.put([-score[i][k], i])  # Negate the value to simulate max heap behavior
        
        # Initialize an empty list to store the sorted result
        result = []    
        
        # Extract elements from the PriorityQueue in sorted order and append corresponding rows to the result list
        while not pq.empty():
            s, r = pq.get()
            result.append(score[r])
        
        # Return the sorted result
        return result
