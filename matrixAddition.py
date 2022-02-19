from termcolor import colored,cprint
cprint('MATRIX OPERATIONS\n_________________','green')
x=int(input("Enter the row:"))
y=int(input("Enter the column:"))
cprint("enter the elemets:",'yellow')
#matrix1=[[int(input("row "))for i in range(x)]for j in range(y)] #this statement is equalent to the input function given below
matrix1=[]
for i in range(x):
    row=[]
    for j in range(y):
        num=int(input("Enter element (%d,%d):"%(i,j)))
        row.append(num)
    matrix1.append(row)
cprint("matrix 1\n________",'yellow')
for i in range(x):
    for j in range(y):
        print(format(matrix1[i][j],"<4"),end=" ")
    print()
#matrix2=[[int(input())for i in range(x)]for j in range(y)]
cprint("\nEnter the matrix 2 elements",'red')
matrix2=[]
for i in range(x):
    row=[]
    for j in range(y):
        num=int(input("Enter element (%d,%d):"%(i,j)))
        row.append(num)
    matrix2.append(row)
cprint("matrix 2\n________",'red')
for i in range(x):
    for j in range(y):
        print(format(matrix2[i][j],"<4"),end=" ")
    print()
cprint("\nRESULTANT MATRIX\n________________",'green')
matrix3=[[0 for i in range(x)]for j in range(y)]
for i in range(x):
    for j in range(y):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(x):
    for j in range(y):
        print(format(matrix3[i][j],"<4"),end=" ")
    print()