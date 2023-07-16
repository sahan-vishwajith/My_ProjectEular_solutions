n=0
x=False
ans=0
while x==False:
    n+=1
    #print(n)
    z=0
    y=False
    while y==False:
       z+=1 
       d=n**z
       
       d=str(d)
       if len(d)==z:
           ans+=1
           print(d)
       if len(d)<z:
           y=True
           break
       if len(d)>z:
           print(d)
           x=True
           break 
print(ans)
