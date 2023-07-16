s2=[]
i=0
def my_function(x):
  return x[::-1]


for n in range(100, 1000):
    for m in range(100, 1000):
        i=m*n

        if int(my_function(str(i))) == i:

            s2.append(i)

print(max(s2))




