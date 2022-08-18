# Q-1 ) 4Sum
# https://leetcode.com/problems/4sum/
# (7.5 marks)
# (Medium)
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
# ● 0 <= a, b, c, d < n
# ● a, b, c, and d are distinct.
# ● nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		Set=set()
		n=len(nums)
		nums.sort()
		for i in range(n):
			for j in range(i+1,n):
				k=j+1
				l=n-1
				while k<l:
					sum=nums[i]+nums[j]+nums[k]+nums[l]
					if sum==target:
						Set.add((nums[i],nums[j],nums[k],nums[l]))
						k=k+1
						l=l-1
					elif sum>target:
						l=l-1
					else:
						k=k+1
		return [list(i) for i in Set]



#  Q-2) Clone Graph (7.5 marks)
# https://leetcode.com/problems/clone-graph/
# (Medium)
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its
# neighbors.
# class Node {
# public int val;
# public List<Node> neighbors;
# }
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For
# example, the first node with val == 1, the second node with val == 2, and so on.
# The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite
# graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the
# copy of the given node as a reference to the cloned graph.
# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = deque([root])
        m = {root: Node(root.val)}
        while queue:
            for neighbor in node.neighbors:
                if neighbor not in m:
                    queue.append(neighbor) 
                    m[neighbor] = Node(neighbor.val)
                m[node].neighbors.append(m[neighbor])
        return m[root]       