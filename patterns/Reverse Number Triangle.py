"""
1 2 3 4
1 2 3
1 2
1
"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()
