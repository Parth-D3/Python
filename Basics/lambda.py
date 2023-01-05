print("---------------PROGRAM FOR LAMBDA(ANONYMOUS) FUNCTIONS---------------")
print("Enter three numbers : ")
a = int(input())
b = int(input())
c = int(input())

max1 = lambda x,y,z: print("X is greatest")  if x>z else print("Z is greatest") if x>y else  print("Y is greatest") if y>z else print("Z is greatest") 
max1(a,b,c)
