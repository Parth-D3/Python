#-------------------BUBBLE SORT--------------------#
n = int(input("Enter Number of Students : "))
marks = [float(input(f"Enter Marks of Student {x + 1} : ")) for x in range(n)]
print("List Entered is : ",marks)

#sorting in ascending order using selection sort
for i in range(n):
    for j in range(0,n-i-1):
        if(marks[j] > marks[j+1]):
            marks[j], marks[j+1] = marks[j+1], marks[j]

print("Sorted list is : ",marks)

#displaying top five scores
print("-----------")
print("No.   Marks")
print("-----------")
rank = 1
for i in range(n-1,n-6,-1):
    print(f"{rank}.   {marks[i]}")
    rank += 1
