#Q-1) Write a program to print the sum of right diagonal of a matrix:
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


#Q-2) Write a program to print sum of border elements of a square Matrix.
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










# Q-3) Write a function to return sum of rows of a matrix as a list
import numpy as np
def rowSum():
    sum = 0
    rows = int(input("rows>> "))
    column = int(input("column>> "))
    val = list(map(int, input("enter vlaue>> ").split()))
    matrix = np.array(val).reshape(rows,column)
    l = list()
    print("\nFinding sum of each row:\n")
    for i in range(rows):
        for j in range(column):
            sum += matrix[i][j]
        l.append(sum)
        sum = 0
    print(matrix, "\nsum of the rows: {}",format(1))
    rowSum()