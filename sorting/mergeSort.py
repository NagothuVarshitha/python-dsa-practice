def merge(l,h,m,a):
    i=l
    j=m+1
    b=[]
    while i<=m and j<=h:
        if a[i]<=a[j]:
            b.append(a[i])
            i+=1
        else:
            b.append(a[j])
            j+=1
    while i<=m:
        b.append(a[i])
        i+=1
    while j<=h:
        b.append(a[j])
        j+=1
    p=l
    for x in range(len(b)):
        a[p]=b[x]
        p+=1
def ms(l,h,a):
    if l<h:
        m=(l+h)//2
        ms(l,m,a)
        ms(m+1,h,a)
        merge(l,h,m,a)
a=[5,2,8,1,9,3]
ms(0,len(a)-1,a)
print("Sorted array:", a)