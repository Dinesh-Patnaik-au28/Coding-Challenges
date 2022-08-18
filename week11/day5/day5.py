#Q-1 ) Climbing Stairs - solve without DP
#https://leetcode.com/problems/climbing-stairs/
#(5 marks)
#(Easy)
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you
#climb to the top?
#Example 1:
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [_ for _ in range(n + 1)]
        for step in range(3, n + 1):
            steps[step] = steps[step - 1] + steps[step - 2]
        return steps[n]


#Q-3 ) Longest Common Subsequence - Solve using DP
#5 marks)
#https://leetcode.com/problems/longest-common-subsequence/
#(Medium)
#Given two strings text1 and text2, return the length of their longest common
#subsequence. If there is no common subsequence, return 0.
#A subsequence of a string is a new string generated from the original string with
#some characters (can be none) deleted without changing the relative order of the
#remaining characters.
#● For example, "ace" is a subsequence of "abcde".
#A common subsequence of two strings is a subsequence that is common to both
#strings.
#Example 1:
#Input: text1 = "abcde", text2 = "ace"
#Output: 3
#Explanation: The longest common subsequence is "ace" and its length is
#3.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text2)][len(text1)]        