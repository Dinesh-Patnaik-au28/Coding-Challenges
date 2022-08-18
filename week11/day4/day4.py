#Q-1 ) Fibonacci Number - solve with DP
#https://leetcode.com/problems/fibonacci-number/
#(5 marks)
#(Easy)
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
#Fibonacci sequence, such that each number is the sum of the two preceding
#ones, starting from 0 and 1. That is,
#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.
#Given n, calculate F(n).
#Example 1:
#Input: n = 2
#Output: 1
#Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
class Solution:
    def fib(self, n: int, lookup={}) -> int:
        if n < 2:
            return n
        if n not in lookup:
            lookup[n] = self.fib(n-1, lookup) + self.fib(n-2, lookup)
        return lookup[n]


#Q-1 ) Fibonacci Number - solve without DP
#https://leetcode.com/problems/fibonacci-number/
#(5 marks)
#(Easy)
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
#Fibonacci sequence, such that each number is the sum of the two preceding
#ones, starting from 0 and 1. That is,
#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.
#Given n, calculate F(n).
#Example 1:
#Input: n = 2
#Output: 1
#Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
class Solution:
    def _fib(self, n: int):
        if n < 2:
            return n, n-1
        a, b = self._fib(n-1)
        return a+b, a
    def fib(self, n: int) -> int:
        a, _ = self._fib(n)
        return a







#Q-3 )Pow(x, n) - Solve using DP (5 marks)
#https://leetcode.com/problems/powx-n/
#(Medium)
#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#Example 1:
#Input: x = 2.00000, n = 10
#Output: 1024.00000
class Solution:
    def myPow(self, x: float, n: int) -> float:
        a=0
        if n ==0:
            return 1
        if n ==1:
            return x
        if n > 0:
            a = self.myPow(x,n//2)
            if n%2==0:
                return a*a
            elif n%2==1:
                return x*a*a
        if n< 0: 
            n=abs(n)
            a = self.myPow(1/x,n//2)
            if n%2==0:
                return a*a
            elif n%2==1:
                return 1/x*a*a