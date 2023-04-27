"""
Problem: https://leetcode.com/problems/roman-to-integer/

Solution: We iterate the string in the reverse order, while keeping track of the max Roman Character we've seen so far.
If any new Roman Character is less than the Max, we subtract it from the total. Otherwise we add to the total.

Time Complexity: O(n) as we iterate over the whole string.

Space Complexity: O(1) as we're only creating 2 variables irrespective of the input size.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        max_sofar = "I"
        total = 0
        for i in s[::-1]:
            if roman_map[i] < roman_map[max_sofar]:
                total -= roman_map[i]
            else:
                max_sofar = i
                total += roman_map[i]
        return total