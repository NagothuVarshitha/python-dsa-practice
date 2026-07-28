"""i/p:145
1! + 4! + 5!
= 1 + 24 + 120
= 145(equal so strong num)
Rule--
Whenever you're calculating something for each item separately, initialize that variable inside the loop."""

n=int(input("Enter a number: "))
temp=n  # Save original number
sum=0   # Store the sum of factorials
while n>0:  # Process every digit
    rem=n%10     # Get the last digit
    # Calculate factorial of this digit
    fact=1  #Every digit starts with a fresh factorial when we initialize this after while loop
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact    # Add factorial to total sum
    n=n//10   # Remove the last digit
if temp==sum:   # Compare original number with sum of factorials
    print("Strong Number")
else:
    print("Not Strong Number")