list = [50, 40, 23, 70, 56, 12, 5, 10,100,200,300, 7]
i=0
max1=0
max2=0
max3=0
max4=0
while(i<len(list)):
    if(list[i]>max1):
        max1=list[i]
    i=i+1
    j=0
    while(j<len(list)):
        if(max1>list[j] and max2<list[j]):
            max2=list[j]
        j=j+1
        k=0
        while(k<len(list)):
            if(max2>list[k] and max3<list[k]):
                max3=list[k]
            k=k+1
            l=0
            while(l<len(list)):
                if (max3>list[l] and max4 <list[l]):
                    max4=list[l]
                l=l+1
print(max1)
print(max2)
print(max3)
print(max4)
