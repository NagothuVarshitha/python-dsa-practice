"""A number is called a Harshad Number if it is completely divisible by the sum of its digits.
Input: 18
Sum of digits = 1 + 8 = 9
18 % 9 = 0
Output: Harshad Number"""
n=int(input("Enter number:"))
temp=n
sum=0   # Variable to store the sum of digits
while n>0:  # Find the sum of all digits
    rem=n%10    # Get the last digit
    sum=sum+rem  # Add it to the sum
    n=n//10      # Remove the last digit
if temp%sum==0:   #Check whether the original number is divisible by the sum of its digits
    print("Harshad Number")
else:
    print("Not Harshad Number")