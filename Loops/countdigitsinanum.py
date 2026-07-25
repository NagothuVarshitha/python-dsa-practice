#i/p:Enter a number: 12345
n=int(input("Enter a number: "))
count=0
"""while n > 0 → Continue until no digits are left.
for i in range(1, n + 1) → Continue until i reaches n."""
while n>0:
    n=n//10
    count+=1
print(count)
