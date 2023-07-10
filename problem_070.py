"""
Problem: https://leetcode.com/problems/climbing-stairs/

Solution: Number of ways to reach a step n would be sum of number of ways to reach n-1 and n-2 steps.

Time Complexity: O(n) as we're iterating n times.

Space Complexity: O(1) as we're using a constant space data structure to keep tarck of steps.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        step_tracker = [1, 2]
        for i in range(n - 2):
            step_tracker.append(step_tracker[0] + step_tracker[1])
            del step_tracker[0]
        
        return step_tracker[-1]