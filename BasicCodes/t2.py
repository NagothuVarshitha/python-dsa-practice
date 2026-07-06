#program to count the number of zeros in the following tuple
t1=tuple(map(int,input("Enter a number: ").split()))
count=0
for i in t1:         #range accepts only by integer so instead of for i in range() use for i in t1:
    if i==0:
        count+=1
print(count)