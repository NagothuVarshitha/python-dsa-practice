#Check that a tuple type cannot be changed in Python


t=tuple(map(int,input("Enter a number: ").split()))
print("original num:",t)
t[0]=100

#o/p gives error as tuple is immutable and the values cant be changed in it

