n=int(input("Enter the number:"))
count=0 #variable counts how many factors a number has.
for i in range(1,n+1):  #loop checks every number from 1 to n.
    count=0
    for j in range(1,i+1):  #This loop finds all factors of i
        if i%j==0:  #Checks whether j is a factor of i.
            count=count+1    #Every time a factor is found, count increase
    if count==2:    #A prime number has exactly 2 factors
        print(i,end=" ")
