class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Initialize a list to store the indices of occurrences of character 'c'
        temp = []
        for i in range(len(s)):
            if s[i] == c:
                temp.append(i)
        
        # Get the length of the input string 's'
        n = len(s)
        
        # Initialize a list to store the distances from each character to the nearest occurrence of 'c'
        dis = [0] * n
        
        # Iterate through each character in the string 's'
        for i in range(n):
            # If the character is not 'c', find the minimum distance to any occurrence of 'c'
            if s[i] != c:
                mn = float('inf')  # Initialize minimum distance to infinity
                for j in temp:
                    mn = min(mn, abs(j-i))  # Update minimum distance
                dis[i] = mn  # Store the minimum distance for the current character
        
        # Return the list of distances
        return dis
