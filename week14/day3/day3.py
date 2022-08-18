# Q-1 ) Minimum Moves to Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# (5 marks)
# (Easy)
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.
# Example 1:
# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments
# two elements):
# [1,2,3] => [2,3,3] => [3,4,3] => [4,4,4
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        for num in nums:
            steps += abs(min_num - num)
        return steps







# Q-2) Longest Substring Without Repeating Characters (5 marks)
# https://leetcode.com/problems/longest-substring-without-repeating-charact
# ers/
# (Medium)
# Given a string s, find the length of the longest substring without repeating
# characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        sub = ''
        res = ''
        for i in s:
            if i not in sub:
                sub += i
            else:
                if len(res) <= len(sub):
                    res = sub
                sub = sub.split(i)[-1] + i
        return max(len(res), len(sub))




# Q-3) Minimum Operations to Reduce X to Zero (5 marks)
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# (Medium)
# You are given an integer array nums and an integer x. In one operation, you can
# either remove the leftmost or the rightmost element from the array nums and
# subtract its value from x. Note that this modifies the array for future operations.
# Return the minimum number of operations to reduce x to exactly 0 if it is
# possible, otherwise, return -1.
# Example 1:
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x
# to zero.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
	    N = len(nums)
	    toremove = sum(nums) - x
	    if toremove < 0: return -1
	    longest_removal = -1
	    left = 0
	    for right in range(N):
		    toremove -= nums[right]
		    while toremove < 0:
			    toremove += nums[left]
			    left += 1
		    if toremove == 0:
			    longest_removal = max(longest_removal, right - left + 1)

	    return N - longest_removal if longest_removal != -1 else -1