# Day 52 
# Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k, n = len(words[0]), len(words)
        need = Counter(words)
        res = []
        for i in range(k):
            left = i
            seen = Counter()
            count = 0
            for j in range(i, len(s) - k + 1, k):
                w = s[j:j+k]
                if w in need:
                    seen[w] += 1
                    count += 1
                    while seen[w] > need[w]:
                        seen[s[left:left+k]] -= 1
                        count -= 1
                        left += k
                    if count == n:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + k
        return res
