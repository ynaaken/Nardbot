import random


def throw_cube():
    cube = random.randint(1, 6)
    return cube

a = [[0 for i in range(2)] for j in range(24)]
a[0][1] = 1
a[0][0] = 15
a[12][1] = 2
a[12][0] = 15
for j in range(2):
    for i in range(24):
        print(a[i][j], end=" ")
    print(" ")

def w(zb,a):
    print("ход белыми на зар:",zb)
    za=-20
    key=0
    for i in range(24):
        if i+zb<24:
            if a[i][1] == 1 and  a[i+zb][1] !=2:
                print("Есть ход c", i," на ", i+zb)
                key=1

    if key == 0:
        print('ходов нет')
    elif key == 1:
        za = int(input())
        while a[za][1] != 1 or a[za+zb][1] ==2 or za+zb>23:
            print("Откуда пойти", zb)
            za = int(input())

        a[za][0] -= 1
        if a[za][0] == 0:
            a[za][1] = 0
        a[za + zb][0] += 1
        if a[za + zb][1] == 0:
            a[za + zb][1] = 1

    for j in range(2):
        for i in range(24):
            print(a[i][j], end=" ")
        print(" ")
    return a


def x(zb,a):
    print("ход черными на зар:",zb)
    key = 0
    za = -1
    for i in range(24):
        if zb + i > 23:
            uda = i + zb - 24
        else:
            uda = i + zb

        if i+zb>11 and i<12:
            h=1 #не нужная переменная
        elif a[i][1] == 2 and a[uda][1] !=1:
            print("Есть ход c", i," на ", uda)
            key=1
    if key == 0:
        print('ходов нет')
    elif key == 1:
        print("Откуда пойти", zb)
        za = int(input())
        if zb + za > 23:
            uda = za + zb - 24
        else:
            uda = za + zb

        a[za][0] -= 1
        if a[za][0] == 0:
            a[za][1] = 0
        a[uda][0] += 1
        a[uda][1] = 2

    for j in range(2):
        for i in range(24):
            print(a[i][j], end=" ")
        print(" ")
    return(a)


while 1>0:
    k = throw_cube()
    k1 = throw_cube()
    print('белые на ',k, k1)
    if k == k1:
        for i in range(4):
            w(k,a)
    else:
        w(k,a)
        w(k1, a)
    k = throw_cube()
    k1 = throw_cube()
    print('черные на ',k, k1)
    if k == k1:
        for i in range(4):
            x(k,a)
    else:
        x(k,a)
        x(k1, a)
