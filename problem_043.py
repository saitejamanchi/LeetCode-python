"""
Problem Statement: https://leetcode.com/problems/multiply-strings/

Solution: We take each number in the forst string from the end and then multiply with the second number.
We then add the result of the above calculation(by taking base of the digit into account like we do while multiplying on a paper) to ge the final result.

Time Complexity: O(m*n) as we have nested loops over the two numbers.

Space Complexity: O(1) as we're creating an integer to keep track of the result but not any other datastructures.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0
        
        curr_pow = 0
        res = 0
        
        for i in num1[::-1]:
            curr = 0
            curr_digit = ord(i) - ord('0')
            for j in num2:
                curr = (curr * 10) + ((ord(j) - ord('0')) * curr_digit)
            res += curr * (10 ** curr_pow)
            curr_pow += 1
            
        return str(res)