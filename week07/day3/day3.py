#Q-1 )Binary Search
#https://leetcode.com/problems/binary-search/
#(Easy)
#(7.5 marks)
#Given an array of integers nums which is sorted in ascending order, and an
#integer target, write a function to search target in nums. If target exists,
#then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.


class solutaion:
    def search(self, nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
nums = list(map(int,input().split()))
target = int(input())
ans = solutaion()
print(ans.search(nums,target))



#Explanation: 2 does not exist in nums so return -1
#Q-2 )Sqrt(x)
#https://leetcode.com/problems/sqrtx/
#(7.5 marks)
#(Easy)
#Given a non-negative integer x, compute and return the square root of x.
#Since the return type is an integer, the decimal digits are truncated, and only the
#integer part of the result is returned.
#Note: You are not allowed to use any built-in exponent function or operator, such
#as pow(x, 0.5) or x ** 0.5.





class solutaion:
    def mysqrt(self, x):
        if (x==0 or x==1):
            return x
        start = 1
        end = x
        while (start <= end):
            mid=(start+end)//2
            if (mid*mid==2):
                return mid
            if (mid*mid<x):
                start = mid+1
                ans = mid
            else :
                end = mid-1
        return ans
x = int(input())
sqr = solutaion()
print(sqr.mysqrt(x))