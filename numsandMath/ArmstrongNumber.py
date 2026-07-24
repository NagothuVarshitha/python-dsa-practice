n=153
x=len(str(n))   #Converts the number to a string.
temp=n  #Stores the original value of n,We need it later because n will become 0 during the loop.
sum=0   #store the sum of the digits raised to the power x.
for i in range(1,n+1): #or while n>0:
    rem=n%10    #Gets the last digit of the number.
    sum=sum+rem**x  #Raises the digit to the power of the number of digits and adds it to sum
    n=n//10 #Removes the last digit.
if temp==sum:   #Compares the original number with the calculated sum.
    print("Armstrong")
else:
    print("Not Armstrong")
