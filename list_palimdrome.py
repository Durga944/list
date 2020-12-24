str=input("enter any str")
i=len(str)-1
new=[]
while(i>=0):
    new.append(str[i])
    i=i-1
print(new)
b=("".join(new))
print(b)
if(str==b):
    print("it is palimdrome")
else:
    print("it is not palimdrome")