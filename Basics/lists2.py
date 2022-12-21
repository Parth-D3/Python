#function to calculate maximum in list     
def calcMax(listA):
     size = 0
     maxA = listA[0]
     for item in listA:
          size += 1

     for i in range(size - 1):
          if(listA[i] < listA [i+1]):
               maxA = listA[i+1]
     return maxA

#----------------------------------------------------------------
# function to calculate average score
def avg(total,x): 
     print("Average Score Is : " ,(total/x))

#----------------------------------------------------------------
# function to calculate highest score
def highest():
     max1 = marks[0]
     for i in range(n):
          if marks[i]!='Ab':
               if max1<marks[i]:
                    max1 = marks[i]
    	
     print("Highest Marks Are : ",max1)

#----------------------------------------------------------------
# function to calculate lowest score
def lowest():
     min1=marks[0]
     for i in range(n):
          if marks[i]!='Ab':
               if min1>marks[i]:
                    min1=marks[i]
    	
     print("Lowest Marks Are : "+str(min1))

#----------------------------------------------------------------
# function to calculate how many students were absent for exam
def countStudents():
     count=0
     for j in range(n):
          if marks[j]=='Ab':
               count += 1
	
     print("Number of Absent Students is : "+str(count))
     
#----------------------------------------------------------------	
# function to calculate marks occuring with highest frequency
def frequency():
     for i in range(n):
          freq = 0
          item = marks[i]
          for j in range(n):
               if item==marks[j]:
                    freq+=1
          occurances.append(freq)	     

     m = occurances.index(calcMax(occurances))

     print("Marks with highest frequency are:-" + str(marks[m]))
 

#----------------------------------------------------------------
# declaring lists
marks=[]
occurances=[]

# getting number of students from user
print("Enter number of students : ")
n = int(input())

sumA=0

print("Enter 'Ab' for absent students")
print("Enter marks of all students")

# input marks
for i in range(n):
	a = input()
	marks += [a]
	if marks[i] != 'Ab':
		sumA = sumA + int(marks[i])

print("Total Marks of All students are : " ,sumA)

#----------------------------------------------------------------
#function calls

avg(sumA,n)
highest()
lowest()
countStudents()
frequency()
