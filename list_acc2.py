a     = [12,0,39,50,1]
kk    = len(a)
new_a = []
i     = 0
while i < kk:
    xx = min(a) 
    new_a.append(xx)
    a.remove(xx)     
    i += 1           
print(new_a)