# declaring empty lists for books and costs
books=[]
costs=[]

# input data
print("Enter Number of Books : ")
n = int(input())

print("Enter Book Names : ")
for i in range(n):
    a = input()
    books += [a]

print("Enter Cost Of Books : ")
for i in range(n):
    c =int(input())
    costs += [c]
    
# display data entered by user
print("Books You Entered Are: \n")
print(books)
print("Costs of The Books Are: \n")
print(costs)
    
# function to remove duplicate entries
def duplicate():
    dup = []
    for item in books:
        if item not in dup:
            dup += [item]
    print("List without duplication is: ", dup)         

# function to arrange in ascending order
def ascending():
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if(costs[j] < costs[minIndex]):
                minIndex = j

        if(minIndex != i):
            books[minIndex],books[i] = books[i],books[minIndex]
            costs[minIndex],costs[i] = costs[i],costs[minIndex]
                    
    print("Sorted List Of Books Is: ",books)

# count number of books with cost more than 500
def countNum():
    count=0
    for i in range(n):
        if costs[i]>500:
            count+=1
    print("Number Of Books With Cost more Than 500 Is: "+str(count))                                    

# create list of books with cost less than 500
def newList():
    list1 = []
    for i in range(n):
        if costs[i]<=500:
            list1 += [books[i]]
            
    print("List of books with cost less than 500 is: ",list1)

# function calls
duplicate()
countNum()
newList()
ascending()
