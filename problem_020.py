"""
Problem: https://leetcode.com/problems/valid-parentheses/

Solution: We iteratively go throu the string, If we come across any open bracket we push it into the stack.
If we get anyclosing bracket, we check the top of the stack for the corresponding opening bracket.
At the end if we have any elements in the stack then it is not a valid string, Otherwise it is valid.

Time Complexity: O(n) as we iterate over the string and fetching from the top of the stack is an constant time operation.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"}": "{", "]":"[", ")":"("}
        stack = []
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i in "}])":
                if not stack or bracket_pairs[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True	