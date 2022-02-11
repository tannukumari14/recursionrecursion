a=[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]
a.remove(11)
a.remove(12)
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
print(b)
i=0
c=[]
while i<len(b):
    if type(b[i])==list:
        j=0
        while j<len(b[i]):
            c.append(b[i][j])
            j+=1
    else:
        c.append(b[i])
    i+=1
i=0
d=[]
while i<len(c):
    if type(c[i])==list:
        j=0
        while j<len(c[i]):
            d.append(c[i][j])
            j+=1
    else:
        d.append(c[i])
    i+=1
print(d)
