list=["durga","sadhvi","sonu","durga","sadhvi","vaibhav","sadhvi"]
i=0
a=[]
while(i<len(list)):
    j=1
    count=0
    while(j<len(list[j])):
        if(list[i]==list[j]):
            count=count+1
        j=j+1
        a.append(list[i])
        a.append(count)
    i=i+1
print(count)