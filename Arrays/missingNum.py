num=[3,0,1,4,5,7,6,9,2]
n=len(num)
total=0     #sum of numbers from 0 to n [0+1+2+3+4+5+6+7+8+9=45]
actual=0    #sum of numbers present in array [3+0+1+4+5+7+6+9+2=37]
for i in range(0,n+1):
    total=total+i
for i in num:
    actual+=i
    missing=total-actual
print(missing)

