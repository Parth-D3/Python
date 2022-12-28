print("This is a program for dividing two numbers")

print("Enter Number 1 : ")
a = int(input())
print("Enter Number 2 : ")
b = int(input())

try:
    c = a/b
    print(c)
except ZeroDivisionError as zd:
    print("ERROR : ",zd)

print("---> DONE <---")
    
