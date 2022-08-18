#Q-1 ) N-Queens
#https://leetcode.com/problems/n-queens-ii/
#(5 marks)
#(Medium)
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard
#such that no two queens attack each other.
#Given an integer n, return the number of distinct solutions to the n-queens
#puzzle.
#Example 1:
#Input: n = 4
#Output: 2
#Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
#Example 2:
#Input: n = 1
#Output: 1

class Solution:
    def totalNQueens(self, n: int) -> int: 
        def rec(col, horizontal, diag, anti_diag):
            if col == n: return 1
            res = 0
            for row in range(n):
                if row not in horizontal and (row + col) not in diag and (row - col) not in anti_diag:
                    horizontal[row] = True; diag[row + col] = True; anti_diag[row - col] = True;
                    res += rec(col + 1, horizontal, diag, anti_diag)
                    del horizontal[row]; del diag[row + col]; del anti_diag[row - col];
            return res
        return rec(0, {}, {}, {})





#Q-2)Sum of All Subset XOR Totals (5 marks)
#https://leetcode.com/problems/sum-of-all-subset-xor-totals/
#(Easy)
#The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if
#the array is empty.
#● For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
#Given an array nums, return the sum of all XOR totals for every subset of nums.
#Note: Subsets with the same elements should be counted multiple times.
#An array a is a subset of an array b if a can be obtained from b by deleting some
#(possibly zero) elements of b.
#Example 1:
#Input: nums = [1,3]
#Output: 6
#Explanation: The 4 subsets of [1,3] are:
#- The empty subset has an XOR total of 0.
#- [1] has an XOR total of 1.
#- [3] has an XOR total of 3.
#- [1,3] has an XOR total of 1 XOR 3 = 2.
#0 + 1 + 3 + 2 = 6
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [[]]
        tot = 0
        for num in nums:
            res += [[num] + i  for i in res ]
        if [] in res:
            res.remove([])
        for r in res:
            tot += functools.reduce(lambda x, y: x^y , r)
        return tot






#Q-3)All Paths From Source to Target (5
#marks)
#ttps://leetcode.com/problems/all-paths-from-source-to-target/
#(Easy)
#Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
#possible paths from node 0 to node n - 1, and return them in any order.
#The graph is given as follows: graph[i] is a list of all nodes you can visit from
#node i (i.e., there is a directed edge from node i to node graph[i][j]).
#Example 1:
#Input: graph = [[1,2],[3],[3],[]]
#Output: [[0,1,3],[0,2,3]]
#Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]], start: int=0) -> List[List[int]]:
        return [[start]+path for paths in [self.allPathsSourceTarget(graph, node) for node in graph[start]] for path in paths] if start < len(graph)-1 else [[start]]                