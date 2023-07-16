x=200
f10=0
f20=0
f50=0
f100=0
for f in reversed(range( (x//100)+1)):
    n=0
    f100=x-100*f

    for l in reversed(range( (f100 // 50)+1 )):
        f50 = f100 - l * 50

        for j in reversed(range( (f50 // 20)+1 )):
            f20 = f50 - j * 20

            for k in reversed(range(  (f20 // 10)+1 )):
                f10 =f20- k * 10
                p5+=1
                for i in reversed(range( (f10 // 5)+1 )):
                    f5 = f10-(i * 5)
                    p5 += f5 // 2

                    p5+=n
                    if f5!=0:
                        p5 += f5 // f5
print(p5)

#73682