a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum1=0
sum2=0
count1=0
count2=0
ave1=0
ave2=0
while(i<len(a)):
    if(a[i]%2==0):
        count1=count1+1
        sum1=sum1+a[i]
        ave1=sum1//count1
    else:
        count2=count2+1
        sum2=sum2+a[i]
        ave2=sum2//count2
        
    i=i+1
print("even",count1)
print("odd",count2)
print(count1+count2)
print("even",sum1)
print("odd",sum2)
print(sum1+sum2)
print("even",ave1)
print("odd",ave2)
print(ave1+ave2)
