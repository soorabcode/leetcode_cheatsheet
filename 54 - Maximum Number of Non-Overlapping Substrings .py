# Day 54
# Maximum Number of Non-Overlapping Substrings
# Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
# The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
# A substring that contains a certain character c must also contain all occurrences of c.

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        intervals = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            i = l
            valid = True
            while i <= r:
                c = s[i]
                if first[c] < l:
                    valid = False
                    break
                r = max(r, last[c])
                i += 1
            if valid:
                intervals.append((l, r))
        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r+1])
                prev_end = r
        return res
