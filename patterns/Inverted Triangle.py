"""
* * * * ---i = 1 → 4 - 1 + 1 = 4
* * *------i = 2 → 4 - 2 + 1 = 3
* *--------i = 3 → 4 - 3 + 1 = 2
*----------i = 4 → 4 - 4 + 1 = 1
"""

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n-i+2): #Why +2? Because Python's range() does not include the ending value.
        print("*",end=" ")
    print()