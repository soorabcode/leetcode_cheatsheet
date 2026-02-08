# Day 55 
# Minimum Insertions to Balance a Parentheses String
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.

# Return the minimum number of insertions needed to make s balanced.   
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0  
        for ch in s:
            if ch == '(':
                need += 2
                if need % 2 == 1:
                    ans += 1
                    need -= 1
            else:
                need -= 1
                if need < 0:
                    ans += 1
                    need = 1
        return ans + need
