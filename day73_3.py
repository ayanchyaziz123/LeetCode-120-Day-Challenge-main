class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string 's' into a list of words
        st = s.split()
        
        # Initialize an empty string to store the result
        res = ""
        
        # Iterate through each word in the list
        for i in range(len(st)):
            # Reverse the current word
            sub = st[i]
            st[i] = sub[::-1]
            
        # Join the reversed words into a single string separated by spaces
        return ' '.join(st)
