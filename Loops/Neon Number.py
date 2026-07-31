"""Neon N.o-sum of the digits of its square is equal to the original number
Input: 9
9² = 81
8 + 1 = 9
Output: Neon Number"""
n=int(input("Enter number:"))
temp=n
sum=0
square=n*n  # Find the square of the number
while square>0:  # Process the digits of the square(we took square  instead of n becoz we should calculate for squ=81 not for n=9)
    rem=square%10
    sum=sum+rem    # Add it to the sum
    square=square//10
if sum==temp:   # Compare the sum with the original number
    print("Neon Number")
else:
    print("Not Neon Number")