# Write a program to print the vowels in a particular str given by the
# user.
str1 = input("Enter the string:") 
str1_lower = str1.lower ()
vowels = "aeiou"
count=0
for i in str1_lower:
    if i in vowels:
        count=count+1
        print(i)
print("count of vowels in the given string:",count)

# Write a program to print sum of n natural numbers .
# Eg n = 5 
n = int(input("enter the number:"))
sum=0
i=1
while (i<=n):
    sum=sum+i
    i=i+1
print("sum=",sum)    


# Write a program in python to find out all the factors of an entered
# number
d = int(input("enter the number:"))
print("factors of" ,d,"is:")
for i in range(1,d+1):
    if d%i==0:
        print(i)





    