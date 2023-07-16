total=0
for i in range(1, 1001):
    total+=i**i
total=str(total)
print(total[-10:-1]+total[-1])
