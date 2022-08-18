#Write a program to print the sum of right diagonal of a matrix
import numpy as np
def slove():
    sum=0
    rows=int(input("rows>> "))
    column=int(input("column>> "))
    val=list(map(int, input("enter value>> ").split()))
    matrix=np.array(val).reshape(rows,column)
    for i in range(rows):
        for j in range(column):
            if ((i+j)==(column-1)):
                sum=sum+matrix[i][j]
    print(matrix, "\nsum of right digonal: {}".format(sum))
slove()


#Write a program to print sum of border elements of a square Matrix
import numpy as np
def slove():
    sum=0
    rows=int(input("rows>> "))
    column=int(input("column>> "))
    val=list(map(int, input("enter value>> ").split()))
    matrix=np.array(val).reshape(rows,column)
    for i in range(rows):
        for j in range(column):
            if (i==0 or j==0 or i==rows-1 or j==column-1):
                sum=sum+matrix[i][j]
    print(matrix, f"\nsum of border elements:{sum}")
slove()






#Q-3 ) Find Peak Element: (3.75)
#https://leetcode.com/problems/find-peak-element/
#(Medium)
#A peak element is an element that is strictly greater than its neighbors.
#Given an integer array nums, find a peak element, and return its index. If the
#array contains multiple peaks, return the index to any of the peaks.
#You may imagine that nums[-1] = nums[n] = -∞.
#You must write an algorithm that runs in O(log n) time.
class solutaion:
    def findpeakelment(self, nums):
        if len(nums) == 1:
            return 0
        for i in range[len(nums)]:
            if i==0:
                if nums[i]>nums[i+1]:
                    return i
            elif i == len(nums)-1:
                if nums[i]>nums[i-1]:
                    return i
            else:
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    return i
nums=list(map(int,input().split()))
p1 = solutaion()
print(p1.findpeakelment(nums))
