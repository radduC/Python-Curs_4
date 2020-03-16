import math


def Curs4_1():

    def A(x):
        print(abs(x) * x ** 3)

    #A = lambda x: abs(x) * x ** 3

    def B(x):
        print(math.log10(x) + math.log(x))

    #B = lambda x: math.log10(x) + math.log(x)

    def C(x):
        print(math.sin(x) + math.sin(x)*math.cos(x))

    #C = lambda x: math.sin(x) + math.sin(x)*math.cos(x)

    def D(x):
        print(math.exp(x) + 2*math.atan(x) - x)

    #D = lambda x: math.exp(x) + 2*math.atan(x) - x

    x = int(input('x = '))
    A(x)
    B(x)
    C(x)
    D(x)


def Curs4_2():
    def aria_dreptunghi(lungime, latime=0):
        if latime == 0:
            aria_dreptunghi(lungime, lungime)
        else:
            print('aria = ', latime * lungime)

    lungime = int(input('lungime = '))
    latime = int(input('latime = '))
    aria_dreptunghi(lungime, latime)


def Curs4_3():
    string = input('string = ')
    for word in string.split():
        print(word)
