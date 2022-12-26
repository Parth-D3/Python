#insertion sort for sorting buckets
def insertionSort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while(j >= 0) and bucket[j] > up:
            bucket[j+1] = bucket[j]
            j -= 1
        bucket[j+1] = up

    return bucket

def bucketSort(x,n, numBuckets):
    maxEle = max(x)
    minEle = min(x)

    limit = (maxEle - minEle) / numBuckets

    temp = []

    for i in range(numBuckets):
        temp.append([])

    for i in range(n):
        diff = (x[i] - minEle) / limit - int((x[i]-minEle) / limit)

        if diff == 0 and x[i] != minEle:
            temp[int((x[i] - minEle) / limit) - 1].append(x[i])
        else:
            temp[int((x[i] - minEle) / limit)].append(x[i])
    
    for i in range(len(temp)):
        temp[i] = insertionSort(temp[i])

    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                x[k] = i
                k += 1

    return x

n = int(input("Enter Number of elements : "))
x = [int(input(f"Enter Element {x+1} : ")) for x in range(n)]
numBuckets = 5
print("Array Entered is : ",x)
print("Sorted Array Is : ",bucketSort(x, n, numBuckets))
