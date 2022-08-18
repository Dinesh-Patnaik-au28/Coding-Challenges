#Check if a number is Palindrome
s = input("enter the value")
reverse = s[::-1]
if(s==reverse):
    print("palindrome")
else:
    print("no palindrome")



#Program for Sum of the digits of a given number
n = int(input())
sum = 0
while n>0:
    reminder = n % 10
    sum = sum + reminder
    n = n//10
print(sum)



#Given a number n, find sum of first n natural numbers
n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("the sum is : ",sum)








#Given two number x and y, find product using
#recursion
def product(a,b):
    if(a<b):
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:
        return 0
a=int(input("enter the first number: "))
b=int(input("enter the sacond number: "))
print("product of the provided number is: ",product(a,b))