x=40
v=int(x/2)
y=1
z=1
permu1=1
permu2=1
for i in range(1, x+1):
    y=y*i
    print(y)
for j in range(1, v+1):
    z=z*j
    print(z)
print('The answer is ', y/(z*z))