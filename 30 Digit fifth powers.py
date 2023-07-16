ans=[]
Rans=0
for n in range(11, 200000):
    n=str(n)
    y=0
    for i in range(len(n)):
        y+=int(n[i])**5
        
        
    if y==int(n):
        
        ans.append(n)
print(ans)
for y in ans:
    Rans+=int(y)
print(Rans)
    
    
