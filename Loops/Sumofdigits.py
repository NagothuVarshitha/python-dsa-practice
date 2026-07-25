n=int(input("Enter a number: "))
sum=0
while n>0:
    ans=n%10
    sum=sum+ans
    n=n//10
print(sum)