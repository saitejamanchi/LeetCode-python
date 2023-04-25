"""
Problem: https://leetcode.com/problems/palindrome-number/
Solution: We find the reverse of the number by iteratively getting digit in the 10's place and forming a new number.
We then compare the original and the new number if they are equal or not.

Time Complexity: O(n) where n is the number of digits inside the number.
Space Complexity: O(1) as we are creating 2 additional variable no matter the input size.


"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_rev = 0
        temp = x
        while x > 0:
            digit = x % 10
            x //= 10
            x_rev = (x_rev * 10) + digit
        return temp == x_rev