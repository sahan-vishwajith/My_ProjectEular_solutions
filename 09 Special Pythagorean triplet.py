x=1
a=0
b=0
z=0
while x==1:
   a+=1

   for b in range(1000):
      if a + b + (a**2+b**2)**0.5 == 1000  :
          c=(a**2+b**2)**0.5
          x = 0
          z = a * b * c
          print(a)
          print(b)

print(z)