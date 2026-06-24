a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
hcf=0
while b != 0:     #Keep going until the remainder becomes 0
    a,b=b,a%b
print("hcf",a)