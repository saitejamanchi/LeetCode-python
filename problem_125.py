"""
Problem: https://leetcode.com/problems/valid-palindrome/

Solution: We take two pointers, one at the beginning of the string and other at the end of the string.
We iteratively check if the two characters are equal or not.
We'll skip the characters if they are not alphanumeric.

Time Complexity: O(n) as we iterative over the string.

Space Complexity: O(1) as we are not creating any additional data structures.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True