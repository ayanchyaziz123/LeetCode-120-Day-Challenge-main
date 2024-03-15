from queue import PriorityQueue

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Create a dictionary to store the frequency of each element in the array
        mp = {}
        for val in arr:
            if val in mp:
                mp[val] += 1
            else:
                mp[val] = 1
        
        # Create a priority queue to store frequencies in descending order
        pq = PriorityQueue()
        for key in mp:
            pq.put(-mp[key])  # Put negative frequencies to make the queue behave like a max heap
        
        cnt = 0  # Initialize the count of elements removed
        n = len(arr)  # Total number of elements in the array
        x = len(arr) // 2  # Target size of the resulting set
        
        # Remove elements from the set until its size becomes less than or equal to x
        while not pq.empty():
            cnt += 1  # Increment the count of elements removed
            val = -pq.get()  # Get the frequency of the next element
            n -= val  # Update the total number of elements remaining
            if n <= x:  # Check if the size of the resulting set is less than or equal to x
                return cnt  # If so, return the count of elements removed
        
        return cnt  # Return the count of elements removed if the loop exits without finding a solution
