#-------------------QUICK SORT--------------------#
n = int(input("Enter Number of Students : "))
marks = [float(input(f"Enter Marks of Student {x + 1} : ")) for x in range(n)]
print("List Entered is : ",marks)

#function for generating partitions of list
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if (array[j] <= pivot):
            i += 1
            array[i],array[j] = array[j],array[i]

    array[i+1], array[high] = array[high],array[i+1]

    return i+1

#function for quick sort
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array,pi + 1, high)

quickSort(marks, 0, n-1)
print("Sorted list is : ",marks)

#displaying top five scores
print("-----------")
print("No.   Marks")
print("-----------")
rank = 1
for i in range(n-1,n-6,-1):
    print(f"{rank}.   {marks[i]}")
    rank += 1

