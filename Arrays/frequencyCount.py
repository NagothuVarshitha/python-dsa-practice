from collections import Counter
arr=[1,2,2,4,4,6,7,7,9]
freq=Counter(arr)
for n,c in freq.items():
    print(n,c)