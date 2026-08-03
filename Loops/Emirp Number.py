"""A number is called an Emirp Number if:
It is a Prime Number.
Its reverse is also a Prime Number.
The reverse should not be equal to the original number.
Input-13
Reverse-31
Check Prime-->13 → Prime ✅
              31 → Prime ✅
              13 ≠ 31
Output: Emirp Number"""

n=int(input("Enter number:"))
temp=n
rev=0
count1=0
count2=0
while n>0:  # Reverse the number
    rem=n%10
    rev=rev*10+rem
    n=n//10
for i in range(1,temp+1):   # Check whether original number is prime
    if temp%i==0:
        count1+=1
for j in range(1,rev+1):    # Check whether reverse number is prime
    if rev%j==0:
       count2+=1
if count1==2 and count2==2 and rev!=temp:   # Check all three conditions
    print("Emirp Number")
else:
    print("Not Emirp Number")

