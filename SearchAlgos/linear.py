#----------------------LINEAR SEARCH-------------------------#
n = int(input("Enter Number of students in class: "))
arr = [int(input(f"Enter Roll No of Student {x + 1}: ")) for x in range(n)]
roll = int(input("Enter Roll No. To Be Searched: "))

#function for linear search
def linearSearch():
    found = False
    for i in range(n):
        if roll == arr[i]:
            print("Roll Number Found At Index: ", i)
            found = True
            break
    if(found == False):
        print("Roll Number Not Found!")    


linearSearch()



