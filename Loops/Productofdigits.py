n=int(input("Enter a number: "))
pro=1
while n>0:
    ans=n%10
    pro=pro*ans
    n=n//10
print(pro)