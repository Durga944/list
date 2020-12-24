a = ["zero","dog","banana","apple","cat"]
b = len(a)
new_a = []
i     = 0
while i < b:
    c = min(a) 
    new_a.append(c)
    a.remove(c)     
    i=i+1          
print(new_a)