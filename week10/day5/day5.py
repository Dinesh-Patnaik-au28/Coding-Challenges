#Q-1 ) Maximum Depth of Binary Tree:
#https://leetcode.com/problems/maximum-depth-of-binary-tree/
#(5 marks)
#(Easy)
#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path
#from the root node down to the farthest leaf node.
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: 3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, depth):
            if not node:
                return depth
            return max(helper(node.left, depth + 1), helper(node.right, depth + 1))
        return helper(root, 0)




#Q-2 ) Invert Binary Tree (5 marks)
#https://leetcode.com/problems/invert-binary-tree/
#(Easy)
#Given the root of a binary tree, invert the tree, and return its root.
#Example 1:
#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]
#Example 2:
#Input: root = [2,1,3]
#Output: [2,3,1]
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        output = TreeNode(root.val)
        output.left = self.invertTree(root.right)
        output.right = self.invertTree(root.left)
        return output

#Q-3)Count Complete Tree Nodes (5 marks)
#https://leetcode.com/problems/count-complete-tree-nodes/
#(Medium)
#Given the root of a complete binary tree, return the number of the nodes in the
#tree.
#According to Wikipedia, every level, except possibly the last, is completely filled
#in a complete binary tree, and all nodes in the last level are as far left as possible.
#It can have between 1 and 2h nodes inclusive at the last level h.
#Design an algorithm that runs in less than O(n) time complexity.
#Example 1:
#Input: root = [1,2,3,4,5,6]
#Output: 6
def countNodes(self, root: Optional[TreeNode]) -> int:
    self.val = 0        
    def func(root):
        if not root:
            return
        self.val+=1
        func(root.left)
        func(root.right)
        func(root)
        return self.val        