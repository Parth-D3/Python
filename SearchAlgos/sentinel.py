#------------------------SENTINEL SEARCH------------------------
n = int(input("Enter Number of Students : "))
listA = [int(input(f"Enter RollNo of Student {x + 1} : ")) for x in range(n)]
item = int(input("Enter RollNo To Be Searched : "))
listA.append(item)
i=0
while(i<n):
    if(listA[i] == item):
        print(f"RollNo is at Index {i}")
        break
    i += 1

print(n)
print(i)
if(i>=n):
    print("RollNo not present in the list")
