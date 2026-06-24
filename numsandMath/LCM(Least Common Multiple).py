a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
x=a
y=b
while y!=0:
    x,y=y,x%y
lcm=(a*b)//x
print("LCM=",lcm)