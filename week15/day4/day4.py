# Q-1 )Binary Search
# https://leetcode.com/problems/binary-search/
# (Easy)
# (7.5 marks)
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1







# Q-2 )Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# (7.5 marks)
# (Easy)
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the
# integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such
# as pow(x, 0.5) or x ** 0.5.
# Example 1:
# Input: x = 4
# Output: 2
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is
# truncated, 2 is returned.
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0 
        high = x
        while low <= high:
            m = (low + high) // 2
            
            if (m * m) > x:
                high = m - 1
                
            elif (m * m) <= x:
                if (m + 1) * (m + 1) > x:
                    return m 
                else:
                    low = m + 1
        