#Q-1 ) Write a program to convert a string of binary number into a decimal
#number: (5 marks) (Easy)
#eg:
#Sample Input
#st = “101”
#Sample output
#5
str = "101"
sum = 0
i = 0
while str!=0:
    rem = str % 10
    sum = sum + rem * pow(2,i)
    str = str (str/10)
    i = i+1
print("decimal number :", sum)





#Q-2 ) Number of 1 Bits: (5 marks) (Medium)
#https://leetcode.com/problems/number-of-1-bits/
#Write a function that takes an unsigned integer and returns the number of '1' bits
#it has (also known as the Hamming weight).
#Example 1:
#Input: n = 00000000000000000000000000001011
#Output: 3
#Explanation: The input binary string 00000000000000000000000000001011 has
#a total of three '1' bits.
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        
        while n:
            if n & 1 == 1:
                # then last bit was 1
                counter += 1
            n = n >> 1
        
        return counter
#Q-3 )Write a function to perform XOR between two positive integers: (5
#marks)
a=5
b=3
print(a^b)