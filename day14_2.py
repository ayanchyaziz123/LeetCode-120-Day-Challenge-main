class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Initialize a boolean array to track visited rooms
        vis = [False] * len(rooms)
        # Use a stack to perform depth-first search starting from room 0
        stack = [0]
        vis[0] = True

        while stack:
            # Pop a room from the stack
            curr = stack.pop()
            
            # Explore keys in the current room
            for key in rooms[curr]:
                if not vis[key]:
                    stack.append(key)
                    vis[key] = True

        # Check if all rooms have been visited
        for i in range(len(vis)):
            if not vis[i]:
                return False

        return True
