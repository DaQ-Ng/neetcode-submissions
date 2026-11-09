from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = dict()
        s2 = dict()
        s1 = Counter(s)
        s2 = Counter(t)
        for c in s:
            if len(s1) != len(s2) or s1[c] != s2[c]:
                return False
        return True
