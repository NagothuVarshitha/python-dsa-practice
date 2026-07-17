n=int(input("Enter a number: "))
a=0     #current Fibonacci number-starts with 0 only
b=1     #next Fibonacci number: 2nd term will be 1 only
for i in range(0,n+1):
    print(a, end="")
    c=a+b
    a=b
    b=c
