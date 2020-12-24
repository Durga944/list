list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
b=[]
while(i<len(list)):
    j=0
    count=0
    a=[]
    while(j<len(list)):
        if(list[i]==list[j]):
            count=count+1
        j=j+1
    a.append(list[i])
    a.append(count)
    i=i+1
    if(a not in b):
        b.append(a)
print(b)