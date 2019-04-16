a=[]
b=[]
count=1
while count<=101:
    if count%2==0:
        a.append(count)
    elif count%2!=0:
        b.append(count)
    count=count+1
print(a)
print(b)