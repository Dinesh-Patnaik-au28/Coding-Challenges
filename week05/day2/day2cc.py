#Let S be a string of length N. Print all the unique substrings of string S
def subString(string):
    n = len(string)
    subS = set()

    for i in range(n):
        for j in range(i+1,n+1):
            temp = (string[i:j])           
            subS.add(temp)
    print(subS)
subString("abb")
#Print a chessboard with N rows and N columns. Each row has alternate white and black cells. The first cell of the first row contains White color
n = 3
for i in range(0,n):
        for j in range(0,n):
            if (i+j)%2==0:
                print("W",end=" ")
            else:
                print("B",end=" ")
        print()
#Let S be a string of length N. Print all the substrings of string S
s = input()
n = len(s)
for i in range(0,n):
    for j in range(i+1,n+1):
        print(s[i:j])