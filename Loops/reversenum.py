n=int(input("Enter: "))
rev=0
"""reverse = reverse * 10 + digit
•  Multiply by 10 → Creates an empty place on the right. 
•  Add the digit → Fills that empty place."""
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)



