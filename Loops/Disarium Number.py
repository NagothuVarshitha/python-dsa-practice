"""Each digit is raised to its position, and the sum equals the original number.
Input:135
Digits are:1 3 5
Positions are:1 2 3
1¹ + 3² + 5³
= 1 + 9 + 125
= 135"""

n=int(input("Enter the number:"))
temp=n
sum=0
digits=0
pos=len(str(n))
while n>0:
    rem=n%10
    digits=digits**pos
    sum=sum+rem
    n=n//10
if temp==sum:
    print("Disarium Number")
else:
    print("Not Disarium Number")
