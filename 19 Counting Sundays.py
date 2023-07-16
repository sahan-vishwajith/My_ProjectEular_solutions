s=[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000]
months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapmonths=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mday=0
days=0
sundays=[6,]
sun=6
answer=0
for i in range(1901, 2000):

    if i in s:
        days+=366

    else:
        days+=365
print(days)
while sun<days:
    sun += 7
    sundays.append(sun)
print(sundays)
for i in range(1901, 2001):
    if i in s:
        for j in leapmonths:
            mday+=j
            if mday in sundays:
                answer+=1

    else:
        for k in months:
            mday+=k
            if mday in sundays:
                answer += 1
print(answer)

