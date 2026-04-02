# day 106 
# Word Ladder 
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    
                    newWord = word[:i] + c + word[i+1:]
                    
                    if newWord == endWord:
                        return level + 1
                    
                    if newWord in wordSet:
                        queue.append((newWord, level + 1))
                        wordSet.remove(newWord)
        
        return 0