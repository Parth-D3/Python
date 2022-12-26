#method for counting sort elements obtained from radix sort 
def countingSort(arr,n,exp1):
    sortedArr = [0]*n
    count = [0]*(10)

    for i in range(n):
        index = arr[i] // exp1
        count[index%10] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = arr[i] // exp1
        sortedArr[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for k in range(n):
        arr[k] = sortedArr[k]

#method for radix sort
def radixSort(arr,n):
    maximum = max(arr)

    exp = 1
    while maximum / exp >= 1:
        countingSort(arr,n,exp)
        exp *= 10

#main body
n = int(input("Enter Number of Elements : "))
arr = [int(input(f"Enter element {x+1} : ")) for x in range(n)]
print("Array Entered is : ",arr)
radixSort(arr,n)
print("Sorted Array is : ",arr)
