#----------------------FIBONACCI SEARCH-------------------------------#
n = int(input("Enter number of students : "))
arr = [int(input(f"Enter Roll Number of Student {x+1} : ")) for x in range(n)]
rollNo = int(input("Enter Roll Number to be Searched : "))

print("List entered is : ",arr)
#sorting list in ascending order
for i in range(n-1):
    minIndex = i
    for j in range(i+1,n):
        if(arr[minIndex] > arr[j]):
            minIndex = j

    if(minIndex != i):
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

print("Sorted List is : ",arr)

#function for fibonacci search
def fiboSearch():
    a = 1
    b = 0
    fib = a + b

    while(fib<n):
        b = a
        a = fib
        fib = a + b

    temp = -1

    while(fib > 1):
        i = min(temp + b, n - 1)
        if(arr[i] < rollNo):
            fib = a
            a = b
            b = fib - a
            temp = i
        elif (arr[i] > rollNo):
            fib = b
            a = a - b
            b = fib - a

        else:
            return i

    if(a and arr[n-1] == rollNo):
        return n - 1

    return -1

loc = fiboSearch()
if(loc == -1): print("Element is not present in the list")
else: print("Element is present at index ->  ",loc)
