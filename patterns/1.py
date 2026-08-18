"""
*       #we have 1 star in row1
* *     #we have 2 star in row2
* * *   #we have 3 star in row3
* * * * #we have 4 star in row4 (so i=1,start=1...)
"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):      # Prints i stars in each row
        print("*",end=" ")
    print()     # Move to the next row