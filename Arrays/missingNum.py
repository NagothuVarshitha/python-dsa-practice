num=[3,0,1,4,5,7,6,9,2]
n=len(num)
total=0
actual=0
for i in range(0,n+1):
    total=total+i
for i in num:
    actual+=i
    missing=total-actual
print(missing)
