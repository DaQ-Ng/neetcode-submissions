class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        right = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in substring:
                substring.discard(s[left])
                left += 1
            substring.add(s[right])
            current = right - left + 1
            if max_length < current:
                max_length = current
        return max_length


