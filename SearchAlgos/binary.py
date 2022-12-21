#----------------------BINARY SEARCH-------------------------------#
n = int(input("Enter Number of Students in Class: "))
arr = [int(input(f"Enter Roll Number of Student {x + 1}: ")) for x in range(n)]
roll = int(input("Enter Roll Number to Be Searched: "))

print("List of Roll Numbers entered is: ",arr)
#sorting in ascending order
for i in range(n - 1):
    minIndex = i
    for j in range(i+1,n):
        if (arr[minIndex] > arr[j]):
            minIndex = j
    if(minIndex != i):
        arr[i], arr[minIndex] = arr[minIndex],arr[i]

print("List after sorting is: ",arr)

#function for binary search
def binarySearch():
    found = False
    left = 0
    right = n-1
    while(left<=right):
        mid = int(( left + right )/2)

        if roll == arr[mid]: 
            found = True
            print(f"Roll number is at index {mid} in the list")
            break;
        elif roll < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if (found == False):
        print("Roll Number is not present in the list")

binarySearch()

    

