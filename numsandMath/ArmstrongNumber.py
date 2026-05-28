n=153
x=len(str(n))
temp=n
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**x
    n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
