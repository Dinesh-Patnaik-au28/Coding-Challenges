#Q-3 ) Divisor Game (solve with DP)
#Easy (5 marks) https://leetcode.com/problems/divisor-game/
#Alice and Bob take turns playing a game, with Alice starting first.
#Initially, there is a number n on the chalkboard. On each player's turn, that
#player makes a move consisting of:
#● Choosing any x with 0 < x < n and n % x == 0.
#● Replacing the number n on the chalkboard with n - x.
#Also, if a player cannot make a move, they lose the game.
#Return true if and only if Alice wins the game, assuming both players play
#optimally.
#Example 1:
#Input: n = 2
#Output: true
#Explanation: Alice chooses 1, and Bob has no more moves.
#Example 2:
#Input: n = 3
#Output: false
#Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more
#moves.
#Marks distribution:
#Question 1,2 and 3 carry 5 marks eac
import math
class Solution:
    def divisorGame(self, n: int) -> bool:
        n = 2
        if n<2:
            return False
        dp=[False]*(n+1)
        dp[2]=True
        for i in range(3,n+1):
            for j in range(1,int(math.sqrt(i))+1):
                if i%j==0 and dp[i-j]==False:
                    dp[i]=True
        return dp[-1]