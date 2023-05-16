"""
Problem: https://leetcode.com/problems/search-insert-position/

Solution: Since we have a sorted array, we try to search for the element similar to binary search.
At the end of the loop if we find the element we can insert at the same position.
If not, then we check if target is less than the mid element. If so, we insert at mid - 1, Otherwise at mid + 1

Time Complexity: O(log n) as it is pretty much similar to the binary search, where we try to divide the current search space into two parts and then continue.

Space Complexity: O(1) as we're not creating any additional data structures.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low  + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        
        if target < nums[mid]:
            return mid
        elif target > nums[mid]:
            return mid + 1