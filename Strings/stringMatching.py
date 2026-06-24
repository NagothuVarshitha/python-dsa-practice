t=input("Enter: ")
s=input("Enter: ")
count=0
for i in range(len(t)-len(s)+1):
    if t[i:i+len(s)]==s:
        count+=1
print(count)

