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







#Find factorial of a number.
number = int(input("enter the number : "))
factorial = 1
if (number < 0):
    print("cant compute factorial for negative numbers")
elif (number < 2):
    print("{}!={}".format(number, factorial))
else:
    for num in range(number, 1, -1):
        factorial = factorial * num
    print("{}! = {}".format(number, factorial))









#Find nth number in fibonacci series.
num = int(input("enter the number :"))
n1, n2 = 0, 1
sum =0
if num<=0:
    print("plase enter number grater than 0")
else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
