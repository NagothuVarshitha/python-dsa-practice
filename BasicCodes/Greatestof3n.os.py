a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))
if a>b and a>c:
    print("a is greater")
elif b>c and b>a:
    print("b is greater")
else:
    print("c is greater")