"""sum of the factorials of its digits equals the original number.
I/P:145
1! + 4! + 5!
= 1 + 24 + 120=145
Output: Peterson Number"""
n=int(input("Enter a number: "))
temp=n
sum=0
while n>0:
    rem=n%10
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if temp==sum:
    print("Peterson Number")
else:
    print("Not a Peterson Number")