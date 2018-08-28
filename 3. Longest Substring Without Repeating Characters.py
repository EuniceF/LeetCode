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
