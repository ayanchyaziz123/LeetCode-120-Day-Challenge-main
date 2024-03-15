from queue import PriorityQueue

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Initialize a priority queue
        pq = PriorityQueue()
        # Add the negative of each input value to the priority queue
        pq.put(-a)
        pq.put(-b)
        pq.put(-c)
        # Initialize the score to 0
        score = 0
        # Loop indefinitely
        while 1:
            # Get the first and second largest values from the priority queue
            val1 = -pq.get()
            val2 = -pq.get()
            # If either value is 0, return the current score
            if val1 == 0 or val2 == 0:
                return score
            # Decrement both values by 1
            val1 -= 1
            val2 -= 1
            # Add the updated values back to the priority queue
            pq.put(-val1)
            pq.put(-val2)
            # Increment the score
            score += 1
        # This line is unreachable because the function always returns within the loop
        return score
