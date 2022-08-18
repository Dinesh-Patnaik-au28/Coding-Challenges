#Q - 2) Longest Substring Without Repeating Characters
#(Medium) (5 marks)
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Given a string s, find the length of the longest substring without repeating
#characters.
#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
class Solution:
    def lenoflongsubstring(self,s:"str")->"int":
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





#Q - 3) Two Sum (5 marks)
#(Easy)
#https://leetcode.com/problems/two-sum/
#Given an array of integers nums and an integer target, return indices of the two
#numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may
#not use the same element twice.
#You can return the answer in any order.
#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]
class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        i = 0 
        j = len(sorted_nums)-1
        s = sorted_nums[i]+sorted_nums[j] 
        while s != target: 
            if s > target:
                j-=1
            else:
                i+=1
            s = sorted_nums[i]+sorted_nums[j]
        x = nums.index(sorted_nums[i])
        nums[x] = -1
        y = nums.index(sorted_nums[j])
        return [y,x]