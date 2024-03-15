#Leetcode problem:-> 383. Ransom Note
#Ayan's code
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
# Initialize frequency arrays for each character (assuming lowercase English letters)
        freq1 = [0] * 26  # to store character frequencies in the magazine
        freq2 = [0] * 26  # to store character frequencies in the ransom note

# Populate freq1 with character frequencies from the magazine
        for i in range(len(magazine)):
            freq1[ord(magazine[i]) - ord('a')] += 1

# Populate freq2 with character frequencies from the ransom note
        for j in range(len(ransomNote)):
            freq2[ord(ransomNote[j]) - ord('a')] += 1

# Compare the frequencies of each character in ransomNote and magazine
        for i in range(26):
            if freq1[i] < freq2[i]:
                return False  # If frequency in magazine is less than ransomNote, return False

        return True  # If all characters in ransomNote can be constructed from magazine, return True
