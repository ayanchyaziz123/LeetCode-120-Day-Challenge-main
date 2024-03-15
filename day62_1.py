from queue import PriorityQueue
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Initialize a priority queue
        pq = PriorityQueue()
        
        # Push the negative of each number into the priority queue
        for num in nums:
            pq.put(-num)
        
        # Initialize the result variable
        res = 0
        
        # Continue until we have processed all k elements
        while k > 0:
            # Retrieve the top element from the priority queue and negate it
            val = -pq.get()
            
            # Add the value to the result
            res += val
            
            # If the value is divisible by 3, divide it by 3 and add the negative of the result back to the priority queue
            if val % 3 == 0:
                pq.put(-(val // 3))
            # If the value is not divisible by 3, divide it by 3, add 1, and add the negative of the result back to the priority queue
            else:
                pq.put(-((val // 3) + 1))
            
            # Decrement the count of elements processed
            k -= 1
        
        # Return the final result
        return res
