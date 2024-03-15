from queue import PriorityQueue
class SeatManager:

    def __init__(self, n: int):
        # Initialize a PriorityQueue to manage available seats
        self.pq = PriorityQueue()
        
        # Populate the PriorityQueue with seat numbers from 1 to n
        for i in range(1, n + 1):
            self.pq.put(i)
        
        # Create a hash array to keep track of reserved seats
        self.hash = [0] * n

    def reserve(self) -> int:
        # Reserve a seat by getting the smallest available seat from the PriorityQueue
        seat = self.pq.get()
        
        # Mark the seat as reserved in the hash array
        self.hash[seat - 1] = 1
        
        # Return the reserved seat number
        return seat

    def unreserve(self, seatNumber: int) -> None:
        # Mark the seat as unreserved in the hash array
        self.hash[seatNumber - 1] = 0
        
        # Put the seat back into the PriorityQueue for future reservations
        self.pq.put(seatNumber)

# Comments have been added to describe each method and the overall logic of the SeatManager class.
