"""
   *
  * * *
 * * * * *
* * * * * * *
 * * * * *
  * * *
   *                (n=4)
   Top: Spaces = n - i
        Stars  = 2*i - 1
   Bottom: Spaces = i
           Stars  = 2*(n-i) - 1
"""
n = int(input("Enter: "))
# ---------- Top half ----------
for i in range(1, n + 1):   # Spaces decrease
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):  # Stars increase
        print("*", end=" ")
    print()
# ---------- Bottom half ----------
for i in range(1, n):   #the middle row is printed only once, so we use (1,n) for the bottom half.
    for j in range(i):  # Spaces increase
        print(" ", end=" ")
    for k in range(2 * (n - i) - 1):    # Stars decrease
        print("*", end=" ")
    print()