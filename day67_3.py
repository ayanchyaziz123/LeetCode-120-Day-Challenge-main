class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the input sentence into individual words
        arr = s.split()
        n = len(arr)
        # Create a list to store the sorted words
        res = [""] * n
        
        # Iterate through each word in the input sentence
        for st in arr:
            m = len(st)
            # Extract the index of the word based on the number at the end
            idx = int(st[m - 1]) - 1
            # Store the word at its corresponding index in the result list
            res[idx] = st[:m - 1]
        
        # Join the sorted words to form the sorted sentence
        return ' '.join(res)
