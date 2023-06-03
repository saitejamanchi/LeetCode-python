"""
Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Solution: We create a min heap based on the initial set fo numbers and then delete the elements that are smaller than the Kth largest element.
This way our Kth largest element would be the first element in our min heap.
As we go on adding the new elements we maintain the heap size to be k by popping the smallest element.
At the end the first element in the heap is the Kth largest element.

Time Complexity: Intially we create min heap using heapify which is a O(m) operation.
Subsequently we add n elements of the stream to the min heap which would take O(n * log(m + n)).
So the overall time complexity would be O(n * log(m + n)).

Space Complexity: Since we create a min heap with m + n elements it would be O(m + n).
"""
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        for i in range(len(nums) - k):
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
