# initializing lists for students playing cricket, badmintoon and football
cricket={'a','b','c','d','w','m','n'}
badminton={'c','e','f','w'}
football={'a','d','e','x','n','o'}

#function for list of students playing both cricket and badminton
def cricBadmin():
    a=[]
    for i in cricket:
        if i in badminton:
            a += [i]
    print("Students Who Play Both Badminton and Cricket are: ",a)

# function for list of students playing eiher cricket or badminton
def cricORBadmin():
    b = []
    for i in cricket:
        if i not in badminton:
            b += [i]
	
    for j in badminton:
        if j not in cricket:
            b += [j]
    print("Students who Either Play Cricket Or Badminton (not both) are: ",b)

# function for number of students playing neither cricket nor badminton
def onlyFootball():
    count1=0
    for i in football:
        if (i not in cricket) and (i not in badminton):
            count1+=1

    print("Number of Students Who Only play Football are: "+str(count1))						
		
# function for number of students playing cricket and football but not badminton		
def cricFootball():
    count2=0
    for i in cricket:
        if i in football and i not in badminton:
            count2+=1			

    print("Number of Students Who Only Play Football and Cricket are: "+str(count2))
			
#function calls
cricBadmin()
cricORBadmin()
onlyFootball()
cricFootball()
			
			
			
			
			
			
			
			
			
			
			
			
			
			

