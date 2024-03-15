class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        if(len(s)) == 1: return True
        cur1 = ord(s[0]) - ord('a')
        cur2 = ord(t[0]) - ord('a')
        for i in range(1, len(s)):
            temp1 = ord(s[i]) - ord('a')
            temp2 = ord(t[i]) - ord('a')
            if cur1 != temp1 or cur2 != temp2:
                return False
            cur1 = temp1
            cur2 = temp2
        return True    