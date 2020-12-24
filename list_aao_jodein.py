a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum1=0
sum2=0
while(i<len(a)):
    if(a[i]%2==0):
        sum1=sum1+a[i]
    else:
        sum2=sum2+a[i]
        
    i=i+1
print(sum1,"even")
print(sum2,"odd")
