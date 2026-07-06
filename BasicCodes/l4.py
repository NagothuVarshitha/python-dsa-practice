"""program to input eight numbers from the user and display all the unique numbers (once)."""

n=list(map(int,input("Enter :").split()))
unique=set(n)
print(*unique)