#Reverse a string using recursion
def reverse_str(str1):
    if str1 == "":
        return ""
    else:
        return reverse_str(str1[1:]) + str1[0]

str1 = input("enter the string:")
str2 = reverse_str(str1)
print("reversed string is :",str2)





#cursive implementation of binary search
def binary_serach(data, low, high, item):
    if low <= high:
        middle = (low+high)//2
        if data[middle] == item:
            return middle
        elif item < data[middle]:
            return binary_serach(data, low, middle-1, item)
        else:
            return binary_serach(data, middle+1, high, item)
    else:
        return -1
nums = [1, 2, 4, 17, 44, 56, 177]
print(binary_serach(nums, 0, len(nums)-1, 177))