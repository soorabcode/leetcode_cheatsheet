# 38 
# Verifying an Alien Dictionary 
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order
# The order of the alphabet is some permutation of lowercase letters 
# Given a sequence of words written in the alien language, and the order of the alphabet 
# return true if and only if the given words are sorted lexicographically in this alien language 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True
