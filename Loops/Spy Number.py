"""sum of its digits is equal to the product of its digits.
Input: 123
Sum = 1 + 2 + 3 = 6
Product = 1 × 2 × 3 = 6
Output: Spy Number"""
n=int(input("Enter a number: "))
temp=n
sum=0
mul=1
while n>0:
    rem=n%10
    sum=sum+rem
    mul=mul*rem
    n=n//10
if sum==mul:
    print("Spy Number")
else:
    print("Not Spy Number")