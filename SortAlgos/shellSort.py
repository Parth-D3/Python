n = int(input("Enter Number of Elements : "))
listA = [int(input(f"Enter Element {x + 1} : ")) for x in range(n)]
print("Array entered is : ",listA)

interval = n//2
while(interval > 0):
    for i in range(n):
        k = i + interval
        if(k<n):
            if(listA[i]>listA[k]):
                listA[i],listA[k] = listA[k],listA[i]
    interval = interval//2

print("Sorted Array is : ",listA)
