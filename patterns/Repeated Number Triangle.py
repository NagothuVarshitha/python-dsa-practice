"""
1
2 2
3 3 3
4 4 4 4
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")    #We want the same value repeatedly, and that value is the row number, so we print i
    print()