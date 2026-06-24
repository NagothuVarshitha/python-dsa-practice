n=153
x=len(str(n))
temp=n
sum=0
for i in range(1,n+1): #or while n>0:
    rem=n%10
    sum=sum+rem**x
    n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
