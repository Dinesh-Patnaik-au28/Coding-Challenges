#Q-1 ) Kth Largest Element in an Array
#https://leetcode.com/problems/kth-largest-element-in-an-array
#/ (5 marks)
#(Medium)
#Given an integer array nums and an integer k, return the kth largest element in
#the array.
#Note that it is the kth largest element in the sorted order, not the kth distinct
#element.
#Example 1:
#Input: nums = [3,2,1,5,6,4], k = 2
#Output: 5
#Example 2:
#Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#Output: 4
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       nums.sort()
       return nums[-k]





#Q-2 )Kth Largest Element in a Stream (5 marks)
#https://leetcode.com/problems/kth-largest-element-in-a-stream/
#(Easy)
#Design a class to find the kth largest element in a stream. Note that it is the
#kth largest element in the sorted order, not the kth distinct element.
#Implement KthLargest class:
#● KthLargest(int k, int[] nums) Initializes the object with the integer k
#and the stream of integers nums.
#● int add(int val) Returns the element representing the kth largest
#element in the stream.
#Example 1:
#Input
#["KthLargest", "add", "add", "add", "add", "add"]
#[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
#Output
#[null, 4, 5, 5, 8, 8]
#Explanation
#KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
#kthLargest.add(3); // return 4
#kthLargest.add(5); // return 5
#kthLargest.add(10); // return 5
#kthLargest.add(9); // return 8
#kthLargest.add(4); // return 8
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k, self.n = k, sorted(nums)
    def add(self, val: int) -> int:
        self.n.insert(bisect.bisect_left(self.n, val, 0, len(self.n)), val)
        return self.n[-self.k]