number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[]
while(i<len(n)):
    j=i+1
    b=[]
    while(j<len(n)):
        sum=n[i]+n[j]
        if(sum==30):
            b.append(n[i])
            b.append(n[j])
        j=j+1
    if(b not in a):
        a.append(b)
    i=i+1
print(a)
    