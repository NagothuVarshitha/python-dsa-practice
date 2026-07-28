#i/p:Enter a number: 12345
n=int(input("Enter a number: "))
count=0
"""while n > 0 → Continue until no digits are left-Use while when you don't know in advance how many times the loop will run.
for i in range(1, n + 1) → Continue until i reaches n-Use for when you already know the number of repetitions."""
while n>0:
    n=n//10
    count+=1
print(count)
