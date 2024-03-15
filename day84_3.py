class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # Initialize a result counter
        res = 0
        
        # Iterate through the list of end times
        for i in range(len(endTime)):
            # Check if the query time falls within the time slot of the student's activity
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                res += 1  # If so, increment the result counter
        
        # Return the total count of students who are busy at the query time
        return res
