# Day 121 
# Valid Parentheses 

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return len(stack) == 0