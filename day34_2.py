import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []

        # Populate the max heap with classes based on their potential increase in pass ratio
        for pass_count, total_count in classes:
            ratio = pass_count / total_count
            heapq.heappush(max_heap, (-((pass_count + 1) / (total_count + 1) - ratio), pass_count, total_count))

        # Assign extra students to classes with the highest potential increase in pass ratio
        while extraStudents > 0:
            _, pass_count, total_count = heapq.heappop(max_heap)
            pass_count += 1
            total_count += 1
            ratio = pass_count / total_count
            heapq.heappush(max_heap, (-((pass_count + 1) / (total_count + 1) - ratio), pass_count, total_count))
            extraStudents -= 1

        # Calculate the average pass ratio across all classes
        average_pass_ratio = sum(pass_count / total_count for _, pass_count, total_count in max_heap) / len(classes)

        return average_pass_ratio
