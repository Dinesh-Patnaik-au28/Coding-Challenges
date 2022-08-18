# Write a program to find the count of all even no’s and odd no’s in an
# array / list
a = [1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for i in range(len(a)):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
print("even: ",even,"odd: ",odd)


#Write a program to find the count of every vowel in a string
str1 = input("Entar the string:")
str1_lower = str1.lower()
vowels = "aeiou"
d = {} .fromkeys(vowels,0)
for i in str1_lower:
    if i in d:
        d[i] = d[i]+1
print(d)

