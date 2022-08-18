# Q-1 )Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sor
# ted-array/
# (7.5 marks)
# (Medium)
# Given an array of integers nums sorted in ascending order, find the starting and
# ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        res=[]
        res.extend([(nums.index(target)),len(nums)-nums[::-1].index(target)-1]) 
        return res



# Q-2 )Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# (7.5 marks)
# (Medium)
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index. If the
# array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left        