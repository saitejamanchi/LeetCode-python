"""
Problem 9: https://leetcode.com/problems/zigzag-conversion/

Solution: We take numRows number of string and iteratively add eac character in the input string in the zig zag manner.

Time Complexity: O(n) as we're iterating over the enire string.

Space Complexity: O(n) as we're creating string which will store all the n characters of the string.
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res_strs = [""] * numRows
        i = 0
        fwd_bwd_flag = 1
        for c in s:
            if i + fwd_bwd_flag == -1 or i + fwd_bwd_flag == numRows:
                fwd_bwd_flag *= -1
            
            res_strs[i] += c
            i += fwd_bwd_flag
             
        return "".join(res_strs)