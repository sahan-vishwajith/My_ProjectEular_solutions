x=0
y=0
for i in range(1, 101):
    x+=i
x=x**2
print(x)
for j in range(1, 101):
    y+=j**2
print(y)
print(x-y)