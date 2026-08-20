"""
* * * * * * *   Row 1 → 7
  * * * * *     Row 2 → 5
    * * *       Row 3 → 3
      *         Row 4 → 1(n=4)
Spaces = i - 1
Stars  = 2*n - 2*i + 1
"""
n=int(input("Enter: "))
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(2*n-2*i+1):
        print("* ",end=" ")
    print()
