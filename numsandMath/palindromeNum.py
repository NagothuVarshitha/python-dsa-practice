n=121
rev=0
temp=n
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
