x=600851475143
prime_val=0
def prime(num):
    """if the number is prime then print 1"""
    if num==1:
        c=0
        return c

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            c = 0
            return c
            break
    else:
        c = 1
        return c

for i in range(1000000):
    print(i)
    if i%2!=0:
        if i%5!=0:
            if 600851475143 % i == 0:
                print(i)
                if prime(i) == 1:
                    prime_val = i
                    print(i)
                    print("done")


print('prime', prime_val)
print('end')


