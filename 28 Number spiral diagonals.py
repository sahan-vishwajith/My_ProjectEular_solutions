from time import time
strt=time()
num = []
for i in range(1, 1002002):
    num.append(i)

posi = [0, ]
n = 0
i = 0
while n != 1002000:
    y = 0
    i += 2
    while y != 4:
        n += i
        posi.append(n)

        y += 1

sum=0
for i in posi:
    sum+=num[i]
end=time()
print(strt-end)
print(sum)
        
