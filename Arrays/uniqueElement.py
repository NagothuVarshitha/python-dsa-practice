from collections import Counter
arr=[1,2,2,3,4,4]
freq=Counter(arr)
for n,c in freq.items():
    if c==1:
        print(n)
