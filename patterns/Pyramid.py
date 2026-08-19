"""
Spaces → 3 2 1 0 → n - i
Stars  → 1 2 3 4 → i
   *
  * *
 * * *
* * * *
"""
n=int(input("Enter: "))
for i in range(1,n+1):
    for j in range(n-i):   
        print(" ",end=" ")
    for j in range(i):
        print("* ",end=" ") #give space after each star to get pyramid with crt spaces
    print()