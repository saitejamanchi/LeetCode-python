"""
Problem: https://leetcode.com/problems/binary-search/

Solution: Just a simple binary search where in we divide the search space into two parts and see where our target might reside in.

Time Complexity: O(log n) as we're dividing or search space in each iteration.

Space Complexity: O(1) as we're not creating any additional data structures.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1