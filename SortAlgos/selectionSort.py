#-------------------SELECTION SORT--------------------#
n = int(input("Enter Number of Students : "))
marks = [float(input(f"Enter Marks of Student {x + 1} : ")) for x in range(n)]
print("List Entered is : ",marks)

#sorting in ascending order using selection sort
for i in range(n - 1):
    minIndex = i
    for j in range(i+1,n):
        if(marks[minIndex] > marks[j]):
            minIndex = j

    if(minIndex != i):
        marks[i], marks[minIndex] = marks[minIndex],marks[i]

print("Sorted list is : ",marks)

#displaying top five scores
print("-----------")
print("No.   Marks")
print("-----------")
rank = 1
for i in range(n-1,n-6,-1):
    print(f"{rank}.   {marks[i]}")
    rank += 1
