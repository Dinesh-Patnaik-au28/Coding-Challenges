#Q-1 )Find the Duplicate Number:
#https://leetcode.com/problems/find-the-duplicate-number/ (Solve the above
#using both the approaches discussed in class) and comment on time
#complexity.
#:(5 marks)
#Given an array of integers nums containing n + 1 integers where each integer is
#in the range [1, n] inclusive.
#There is only one repeated number in nums, return this repeated number.
#You must solve the problem without modifying the array nums and uses only
#constant extra space.
#Example 1:
#Input: nums = [1,3,4,2,2]
#Output: 2
List = [1,3,4,2,2]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = abs(nums[i])
            if nums[a]<0:
                return a
            else:
                nums[a] = -1*nums[a]

#Q-3 ) Longest Common Prefix:
#https://leetcode.com/problems/longest-common-prefix/submissions/
#(5 marks)
#Write a function to find the longest common prefix string amongst an array of
#strings.
#If there is no common prefix, return an empty string "".
#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return '' 
        res = ''
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(res+i):
                res += i
            else:
                break
        return res