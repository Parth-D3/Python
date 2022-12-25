n = int(input("Enter number of Elements : "))
arr = [int(input(f"Enter Element {x+1} : ")) for x in range(n)]
print("Array Entered Is: ",arr)

for i in range(n-1):
    j = i
    while (j>=0):
        if(arr[j]>arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        j-=1

print("Sorted Array is: ",arr)
