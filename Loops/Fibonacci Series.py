n=int(input("Enter a number: "))
a=0 # First Fibonacci number
b=1 # Second
print(a,end=" ")    # Print the first number
print(b,end=" ")
# We have already printed 2 numbers,
# so generate the remaining (n-2) numbers
for i in range(1,n-1):
        c=a+b     # Current Fibonacci number = previous two numbers
        a=b
        b=c
        print(c,end=" ")