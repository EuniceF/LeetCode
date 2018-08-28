class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        start = maxlen = 0
        for i, val in enumerate(s):
            if val in used and start <= used[val]:
                start = used[val] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            used[val] = i
        return maxlen
# Tips:
# How to check that the char shows before in the new start substring?
# e.g. "abba" -> in "ba", 'a' only happens once, how to avoid counting twice for 'a' cuz 'a' also happens in index 0.
# solutions:
# In if statement, we need to add "start <= used[va]" to check whether the char happens before in the new start substring.
