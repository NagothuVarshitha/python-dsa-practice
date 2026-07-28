n=int(input("Enter a number: "))
temp=n  # Save original number
digit=len(str(n))   # Count digits
sum=0   # Store Armstrong sum
while n>0:  # Process every digit
    rem=n%10   # Get last digit
    sum=sum+rem**digit  # Add digit^number_of_digits
    n=n//10 # Remove last digit
if temp==sum:   #Compare original number with Armstrong sum
    print("Armstrong Number")
else:
    print("Not Armstrong Number")