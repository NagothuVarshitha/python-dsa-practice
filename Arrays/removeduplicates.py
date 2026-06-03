arr=[1,2,2,3,4,4]
b=[]
for i in arr:
    if i not in b:
        b.append(i)
print(b)