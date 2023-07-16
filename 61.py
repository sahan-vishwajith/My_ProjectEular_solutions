from itertools import permutations


def link(x, y):
    X = str(x)
    X = X[2:4]
    Y = str(y)
    Y = Y[0:2]
    if Y == X:
        return True
    else:
        return False

def n(i,q):
    if i==3:
        x=((((2 * q) + 0.25) ** 0.5) + 0.5)
        return x
    if i ==4:
        x=((q) ** 0.5)
        return x
    if i ==5:
        x=((((q / 3) + (1 / 36)) ** 0.5) + (1 / 6))
        return x
    if i ==6:
        x=((((q/ 2) + (1 / 16)) ** 0.5) + (1 / 4))
        return x
    if i ==7:
        x=(((((2 * q) / 5) + (9 / 100)) ** 0.5) + (3 / 10))
        return x
    if i ==8:
        x=((((q / 3) + (4 / 36)) ** 0.5) + (2 / 6))
        return x
list3 = [3,]
list4 = [4,]
list5 = [5,]
list6 = [6,]
list7 = [7,]
list8 = [8,]


for i in range(int((((2 * 999) + 0.25) ** 0.5) - 0.5) - 5, int((((2 * 9999) + 0.25) ** 0.5) - 0.5) + 5):
    x = int((i * (i + 1)) / 2)

    if len(str(x)) == 4:
        list3.append(x)
for i in range(int((999) ** 0.5) - 5, int((9999) ** 0.5) + 5):
    x = int(i ** 2)

    if len(str(x)) == 4:
        list4.append(x)
for i in range(int((((999 / 3) + (1 / 36)) ** 0.5) + (1 / 6)) - 5, int((((9999 / 3) + (1 / 36)) ** 0.5) + (1 / 6)) + 5):
    x = int((i * (3 * i)) - 1)

    if len(str(x)) == 4:
        list5.append(x)
for i in range(int((((999 / 2) + (1 / 16)) ** 0.5) + (1 / 4)) - 6, int((((9999 / 2) + (1 / 16)) ** 0.5) + (1 / 4)) + 6):
    x = int(i * ((2 * i) - 1))

    if len(str(x)) == 4:
        list6.append(x)
for i in range(int(((((2 * 999) / 5) + (9 / 100)) ** 0.5) + (3 / 10)) - 7,int(((((2 * 9999) / 5) + (9 / 100)) ** 0.5) + (3 / 10)) + 5):
    x = int((i * ((5 * i) - 3)) / 2)

    if len(str(x)) == 4:
        list7.append(x)
for i in range(int((((999 / 3) + (4 / 36)) ** 0.5) + (2 / 6)) - 5, int((((9999 / 3) + (4 / 36)) ** 0.5) + (2 / 6)) + 5):
    x = int(i * ((3 * i) - 2))

    if len(str(x)) == 4:
        list8.append(x)

listall = []
listall.append(list3)
listall.append(list4)
listall.append(list5)
listall.append(list6)
listall.append(list7)
x=0
listx = list(permutations(listall, 5))
#print(list8)
for e in listx:
    li3 = e[1] +  e[3] + e[4] + list8
    li4 = e[0] + e[2] + e[3] + e[4] + list8
    li5 = e[0] + e[1] + e[3] + e[4] + list8
    li6 = e[0] + e[2] + e[1] + e[4] + list8
    li7 = e[0] + e[2] + e[3] + e[1] + list8
    li8 = e[0] + e[2] + e[3] + e[4] + e[1]
    for z in list8:
        for q in e[0]:
            if link(z, q) == True :
                for w in e[1]:
                    if link(q, w) == True and w not in li4:
                        for r in e[2]:
                            if link(w, r) == True and r not in li5:
                                for t in e[3]:
                                    if link(r, t) == True and t not in li6:
                                        for y in e[4]:
                                            if link(t, y) == True and y not in li7:
                                                if link(y, z) == True and z not in li8:
                                                    if x==0:
                                                        li3 = e[1] + e[2] + e[3] + e[4] + list8
                                                        li4 = e[0] + e[2] + e[3] + e[4] + list8
                                                        li5 = e[0] + e[1] + e[3] + e[4] + list8
                                                        li6 = e[0] + e[2] + e[1] + e[4] + list8
                                                        li7 = e[0] + e[2] + e[3] + e[1] + list8
                                                        li8 = e[0] + e[2] + e[3] + e[4] + e[1]
                                                        print(z, q, w, r, t, y)
                                                        x=1

                                                        print(z + q + w + r + t + y)


