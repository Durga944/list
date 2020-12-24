a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count1=0
count2=0
while(i<len(a)):
    if(a[i]%2==0):
        count1=count1+1
    else:
        count2=count2+1
        
    i=i+1
print(count1,"even")
print(count2,"odd")
