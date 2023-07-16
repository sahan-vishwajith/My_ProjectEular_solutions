import math
s=0
z=0
for i in reversed(range(100000, 1000000)):
    x=i

    y=0
    while x!=1:
        v = math.log2(x)
        if v // 1 == v:
            y+=v

            x=1
        elif x % 2 != 0:
            x = 3 * x + 1
            y+=1
        else:
            x = x / 2
            y+=1
    if z<=y:
        z=y
        s=i

print(z, '-', s)
