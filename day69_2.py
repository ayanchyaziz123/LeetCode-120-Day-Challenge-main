from queue import PriorityQueue

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Initialize the result list with empty strings
        res = [""] * len(score)
        
        # Create a priority queue to store scores and their indices
        pq = PriorityQueue()
        
        # Insert scores into the priority queue along with their indices
        for i in range(len(score)):
            pq.put([-score[i], i])  # Use negative scores for reverse ordering
        
        # Initialize the rank
        rank = 1
        
        # Process each score from the priority queue
        while not pq.empty():
            # Get the score and index from the priority queue
            val, ind = pq.get()
            
            # Assign the rank based on its position in the sorted order
            if rank == 1:
                res[ind] = "Gold Medal"
            elif rank == 2:
                res[ind] = "Silver Medal"
            elif rank == 3:
                res[ind] = "Bronze Medal"
            else:
                res[ind] = str(rank)
            
            # Increment the rank for the next score
            rank += 1
        
        # Return the result list
        return res
