#Q-2 )Palindrome Number - Try using BFS in this (5 marks)
#https://leetcode.com/problems/palindrome-number/
#(Easy)
#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For
#example, 121 is palindrome while 123 is not.
#Example 1:
#Input: x = 121
#Output: true
#Example 2:
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
#Therefore it is not a palindrome.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]




#Q-3 ) Binary Tree Zigzag Level Order Traversal (5 marks)
#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#(Medium)
#Given the root of a binary tree, return the zigzag level order traversal of its nodes'
#values. (i.e., from left to right, then right to left for the next level and alternate
#between).
#Example 1:
#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[20,9],[15,7]]
#Example 2:
#Input: root = [1]
#Output: [[1]]
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        c=0
        val=[root.val]
        l=[]
        queue = [root]
        while (queue):
            c+=1
            if(c%2==0):
                val.reverse()
            l.append(val)
            val=[]
            for i in range (len(queue)):
                x = queue.pop(0)
                if(x.left or x.right):
                    if x.left:
                        queue.append(x.left)    
                        val.append(x.left.val)
                    if x.right:
                        queue.append(x.right)
                        val.append(x.right.val)               
        return l        