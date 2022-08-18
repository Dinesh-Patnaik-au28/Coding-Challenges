#Q-2 ) Min Stack: (5 marks) https://leetcode.com/problems/min-stack/
#(Easy)
#Design a stack that supports push, pop, top, and retrieving the minimum
#element in constant time.
#Implement the MinStack class:
#● MinStack() initializes the stack object.
#● void push(val) pushes the element val onto the stack. ●
#void pop() removes the element on the top of the stack. ●
#int top() gets the top element of the stack.
#● int getMin() retrieves the minimum element in the stack.
#Example 1:
#Input
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]
#Output
#[null,null,null,null,-3,null,0,-2]
#Explanation
# minStack = new MinStack();
#minStack.push(-2);
#minStack.push(0);
#minStack.push(-3);
#minStack.getMin(); // return -3
#minStack.pop();
#minStack.top(); // return 0
#minStack.getMin(); // return -2
class MinStack:
    def __init__(self):
        self.stack=[(-1,float('inf'))]
    def push(self, x: int) -> None:        
        if x<self.stack[-1][1]:
            self.stack.append((x,x))
        else:
            self.stack.append((x,self.stack[-1][1]))
    def pop(self) -> None:
         self.stack.pop()[0]
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
#Q-3 )Trapping Rain Water (5 marks)
#https://leetcode.com/problems/trapping-rain-water/
#(Hard)
#Given n non-negative integers representing an elevation map where the width of
#each bar is 1, compute how much water it can trap after raining.
#Example 1:
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by
#array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are
#being trapped.
#Example 2:
#Input: height = [4,2,0,3,2,5]
#Output: 9
List = [0,1,0,2,1,0,1,3,2,1,2,1]
List2 = [4,2,0,3,2,5]
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1,len(height)-1): 
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            potential = min(max_left, max_right) - height[i]
            ans += max(0, potential) 
        return ans