from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # Function to check if a query matches the pattern
        def is_match(query, pattern):
            i, j = 0, 0

            # Iterate through the characters of query and pattern
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].isupper():
                    return False  # If a uppercase letter doesn't match, return False
                else:
                    i += 1

            # Check remaining characters in query for uppercase letters
            while i < len(query):
                if query[i].isupper():
                    return False  # If there are remaining uppercase letters, return False
                i += 1

            return j == len(pattern)  # Return True if pattern is fully matched

        result = []

        # Check each query against the pattern and append the result to the list
        for query in queries:
            result.append(is_match(query, pattern))

        return result
