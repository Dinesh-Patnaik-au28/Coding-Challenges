#Q-1 ) Valid Parentheses:
#https://leetcode.com/problems/valid-parentheses/
#(5 marks)
#(Easy)
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
#the input string is valid.
#An input string is valid if:
#1. Open brackets must be closed by the same type of brackets.
#2. Open brackets must be closed in the correct order.
#Example 1:
#Input: s = "()"
#Output: true
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        for i in range(length):
            stack_len = len(stack)
            if stack_len == 0:
                stack.append(s[i])
            elif s[i] == ")" and stack[stack_len-1] == "(":
                stack.pop(stack_len-1)
            elif s[i] == "}" and stack[stack_len-1] == "{":
                stack.pop(stack_len-1)
            elif s[i] == "]" and stack[stack_len-1] == "[":
                stack.pop(stack_len-1)
            else:
                stack.append(s[i])
        return len(stack) == 0




#Q-2 )Baseball Game: (5 marks) https://leetcode.com/problems/baseball-game/
#(Easy)
#You are keeping score for a baseball game with strange rules. The game
#consists of several rounds, where the scores of past rounds may affect future
#rounds' scores.
#At the beginning of the game, you start with an empty record. You are given a list
#of strings ops, where ops[i] is the ith operation you must apply to the record and
#is one of the following:
#1. An integer x - Record a new score of x.
#2. "+" - Record a new score that is the sum of the previous two scores. It is
#guaranteed there will always be two previous scores.
#3. "D" - Record a new score that is double the previous score. It is
#guaranteed there will always be a previous score.
#4. "C" - Invalidate the previous score, removing it from the record. It is
#guaranteed there will always be a previous score.
#Return the sum of all the scores on the record.
#Example 1:
#Input: ops = ["5","2","C","D","+"]
#Output: 30
#Explanation:
#"5" - Add 5 to the record, record is now [5].
#"2" - Add 2 to the record, record is now [5, 2].
#"C" - Invalidate and remove the previous score, record is now [5].
#"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
#"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
#The total sum is 5 + 10 + 15 = 30.
List = ["5","2","C","D","+"]
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for i in ops:
            if i not in ["+", "D", "C"]:
                records.append(int(i))
            elif i == "D":
                records.append(2 * records[-1])
            elif i == "C":
                records.pop()
            elif i == "+":
                records.append(records[-1] + records[-2])
        return sum(records)







#Q-3 )Remove All Adjacent Duplicates In String (5 marks)
#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/ (Easy)
#You are given a string s consisting of lowercase English letters. A duplicate
#removal consists of choosing two adjacent and equal letters and removing them.
#We repeatedly make duplicate removals on s until we no longer can.
#Return the final string after all such duplicate removals have been made. It can
#be proven that the answer is unique.
#Example 1:
#Input: s = "abbaca"
#Output: "ca"
#Explanation:
#For example, in "abbaca" we could remove "bb" since the letters are adjacent
#and equal, and this is the only possible move. The result of this move is that the
#string is "aaca", of which only "aa" is possible, so the final string is "ca".
class Solution:
    def removeDuplicates(self, s: str) -> str:
        idx = 0
        n = len(s)-1
        while idx < n:
            if s[idx] == s[idx+1]:
                s = s[:idx] + s[idx+2:]
                idx = idx - 1 if idx else 0
                n -= 2
            else:
                idx += 1
        return s