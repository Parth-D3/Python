print("Program to implement Exception Class and related concepts")

a= 10
    
try:
    #ZeroDivisionError
    c = a/0

    #TypeError
    sum1 = "Python" + []

    #NameError
    print(var)

    print("2+2 = 5")

except Exception as ex:
    print("ERROR : ",ex)

else:
    print("Program Executed Successfully")

finally:
    print("Done.")

print("------------------------------------------")
