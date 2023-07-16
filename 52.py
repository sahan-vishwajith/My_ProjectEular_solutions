def le(x):
    z=list(str(x))
    y=sorted(z)
    return y
b=False
n=0
while b==False:
   n+=1
   m=n*2
   if le(m)==le(n):
       m=n*3
       if le(m) == le(n):
           m=n*4
           if le(m) == le(n):
               m=n*5
               if le(m) == le(n):
                   m=n*6
                   if le(m) == le(n):
                       print(n)
                       b=True
                       break