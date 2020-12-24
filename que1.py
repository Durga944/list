a = [10, 32, 42, 65, 67, 89, 76, 38, 67]
i=0
count=0
sum=0
total=0
while(i<len(a)):
    total=total+a[i]
    count=count+1
    sum=sum+total
    i=i+1
print(total//i)