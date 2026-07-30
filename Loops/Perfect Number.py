"""Perfect Number-sum of its factors equals the number
i/p-6
factors of 6-1,2,3(We don't include the number itself)
Now add them:1 + 2 + 3 = 6"""

n=int(input("Enter: "))
temp=n  # Store the original number
sum=0   # Variable to store the sum of factors
for i in range(1,n):    # Check every number from 1 to n-1
    if n%i==0:  # If i divides n completely, then it is a factor
        sum=sum+i   # Add the factor to the sum
if temp==sum:   # Compare the sum of factors with the original number
    print("Perfect Number")
else:
    print("Not Perfect Number")

