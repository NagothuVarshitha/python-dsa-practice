"""Perfect Number-sum of its factors equals the number
i/p-6
factors of 6-1,2,3(We don't include the number itself)
Now add them:1 + 2 + 3 = 6"""

n=int(input("Enter: "))
temp=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if temp==sum:
    print("Perfect Number")
else:
    print("Not Perfect Number")

