n=int(input("Enter the number:"))
sum=0
while n>0:
    rem=n%10
    if rem%2!=0:
        sum=sum+rem
    n=n//10
print(sum)
