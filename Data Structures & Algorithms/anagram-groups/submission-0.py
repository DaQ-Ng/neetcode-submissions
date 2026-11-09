from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            anagram[key].append(strs[i])
        return list(anagram.values())

