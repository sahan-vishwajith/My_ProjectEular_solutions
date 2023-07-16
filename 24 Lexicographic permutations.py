x=('0123456789')
time=999999
y=0
z=0
k=''
ans=0
for f in range(time):
    for i in reversed(range(10)):
        if x[i-1]<x[i]:
          
            y=(x[i-1])
            break
    for j in reversed(range(10)):
        if y<x[j]:
            y=(x[j])
            
            break
    x=list(x)
    
    x[i-1], x[j]= x[j], x[i-1]
    x=k.join(x)
    x=x[0:i]+x[10:i-1 : -1]     
    
    
    x=str(x)
    
    
print(x)
