import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        n = len(heights)
        bricks_used = 0  # Keep track of bricks used so far
        ladder_heap = []  # Priority queue to store height differences

        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]  # Calculate the difference in heights

            if height_diff > 0:  # If the next building is taller
                heapq.heappush(ladder_heap, height_diff)  # Push the height difference onto the heap
                if len(ladder_heap) > ladders:  # If there are more height differences than available ladders
                    bricks_used += heapq.heappop(ladder_heap)  # Use bricks to cover the difference
                if bricks_used > bricks:  # If the bricks used exceed the available bricks
                    return i  # Return the index of the last reachable building

        return n - 1  # If all buildings are reachable, return the index of the last building
