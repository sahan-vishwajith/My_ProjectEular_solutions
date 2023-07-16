from itertools import permutations
num=[0,1,2,3,4,5,6,7,8,9]
numbers=[list(permutations(num, 10))]
#print(numbers)

'''d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17'''
def div(c):
    x1=str(c[1])+str(c[2])+str(c[3])
    x2 = str(c[2]) + str(c[3]) + str(c[4])
    x3 = str(c[3]) + str(c[4]) + str(c[5])
    x4 = str(c[4]) + str(c[5]) + str(c[6])
    x5 = str(c[5]) + str(c[6]) + str(c[7])
    x6 = str(c[6]) + str(c[7]) + str(c[8])
    x7 = str(c[7]) + str(c[8]) + str(c[9])
    if int(x1)%2==0:
        if int(x2) % 3 == 0:
            if int(x3) % 5 == 0:
                if int(x4) % 7 == 0:
                    if int(x5) % 11 == 0:
                        if int(x6) % 13== 0:
                            if int(x7) % 17 == 0:
                                return True
    else:
        return False

total=0
for n in numbers:
    for v in n:
        if div(v)==True:
            i=''
            for z in v:
                i+=str(z)
            total+=int(i)
print(total)