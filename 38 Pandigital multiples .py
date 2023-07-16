max=0
m=0
for n in range(5000, 50000):
    v = ''
    for i in range(1, 3):
        v += str(n * i)
    lists = sorted(list(v))

    x = ['1', '2', '3', '4', '5', '6','7', '8', '9']
    if lists == x:
        if max<n:
            max=n
            m=v
print(m)
