a = ["zzzzzz","dog","banana","apple","cat"]
i = 0
while i < len(a):
    j=i+1
    while(j<len(a)):
        if a[i]>a[j]:
            var=a[i]
            a[i]=a[j]
            a[j]=var
        j=j+1
    i=i+1
print(a)
        
          
        