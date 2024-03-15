from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Create a queue with (person index, tickets left) pairs
        queue = [(i, tickets[i]) for i in range(len(tickets))]
        time = 0

        while True:
            person, ticket_left = queue.pop(0)
            # Check if the desired person (k) has bought all tickets
            if person == k and ticket_left == 0:
                return time
            # If the person still has tickets, update the queue
            if ticket_left > 0:
                # If the person is the desired one and has one ticket left, return with the updated time
                if person == k and ticket_left == 1:
                    return time + 1

                # If the person has more than one ticket left, update the queue
                if ticket_left > 1:
                    queue.append((person, ticket_left - 1))
            # Increment the time for every iteration
            time += 1

        return time  # This line will not be reached, but it's kept for completeness
