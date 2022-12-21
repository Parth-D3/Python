# initialing empty lists for matrices
matrixA = []
matrixB = []
result = []
#-----------------------------------------------------
# input data
print("Enter number of rows for matrix")
row = int(input())
print("Enter number of columns for matrix")
col = int(input())

# entering two matrics
print(f"Enter two matrices of order {row} x {col}: ")
print("Matrix A")
for i in range(row):
    temp = []
    for j in range(col):
        ele = int(input())
        temp += [ele]
    matrixA += [temp]

print("Matrix B")
for i in range(row):
    temp = []
    for j in range(col):
        ele = int(input())
        temp += [ele]
    matrixB += [temp]
#-----------------------------------------------------
# defining function to print matrix
def printData(listA):
    for i in range(row):
        for j in range(col):
            print(listA[i][j],end=" ")
        print("")

# diplaying matrices entered by the user
print("Matrices You Entered Are: ")
print("Matrix A")
printData(matrixA)
print("Matrix B")
printData(matrixB)
#-----------------------------------------------------
# adding the two matrices
print("Addition of these two matrices is : ")
for i in range(row):
    for j in range(col):
        print(matrixA[i][j] + matrixB[i][j],end = " ")
    print("")
#-----------------------------------------------------
# substracting the two matrices
print("Substraction of these two matrices is : ")
for i in range(row):
    for j in range(col):
        print(matrixA[i][j] - matrixB[i][j],end = " ")
    print("")
#-----------------------------------------------------
#multiplying the two matrices
# creating a matrix with all elements zero to store product
for i in range(row):
    temp = []
    for j in range(col):
        a = 0
        temp += [a]
    result += [temp]

# calculating product
print("Multiplication of these two matrices is : ")
# iterate through rows of matrixA
for i in range(row):
   # iterate through columns of matrixB
   for j in range(col):
       # iterate through rows of matrixB
       for k in range(row):
           result[i][j] += matrixA[i][k] * matrixB[k][j]

printData(result)
#-----------------------------------------------------
# transpose of matrixA
print("Transpose of matrix A : ")
for i in range(row):
    for j in range(col):
        result[i][j] = matrixA[j][i]

printData(result)
#-----------------------------------------------------           


