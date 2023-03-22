import random
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation


def binaryTodecimal(n):  # função de converção binaria para decimal
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2
    return decimal


def convert(list):  # função de converter uma lista de um tipo, para uma lista de inteiro
    res = int("".join(map(str, list)))
    return res


def numConcat(num1, num2):  # função para concatenar listas
    digits = len(str(num2))
    num1 = num1 * (10**digits)
    num1 += num2
    return num1


def zeroToCrom(list, num1):
    for i in range(num1):
        if (i == 1 or i == 3):
            list[i] = 1
        else:
            list[i] = 0
    return list


def initInd(list, num1):
    for j in range(num1):
        a = random.uniform(0, 1)
        if (a >= 0.5):
            list[j] = 1
        else:
            list[j] = 0
    return list


def arredondar(list, num1):
    aux = initInd(list, num1)
    return aux


def oneToCrom(list, num1):
    for i in range(num1):
        if (i == 0 or i == 1 or i == 3):
            list[i] = 1
        else:
            list[i] = 0
    return list


def initPop(list, num1, num2):
    for i in range(num1):
        for j in range(num2):
            a = random.uniform(0, 1)
            if (a >= 0.5):
                list[i][j] = 1
            else:
                list[i][j] = 0
    return list


def binToDec(pop_x, pop_y, melhor_X, melhor_Y, sinal_X, sinal_Y, real_X, real_Y, Count, numC, numP):
    indX = numpy.zeros(numC)
    indY = numpy.zeros(numC)
    for i in range(numP):
            indX[:] = pop_x[i, :]
            indY[:] = pop_y[i, :]
            auxConv = 0
            auxConv2 = 0
            sinal_X[i] = indX[29]
            sinal_Y[i] = indY[29]

            for j in range(numC):
                auxConv = auxConv+indX[j]*(2**(numC-(j+1)))
                auxConv2 = auxConv2+indY[j]*(2**(numC-(j+1)))

            real_X[i] = (10/(2**numC-1))*auxConv
            real_Y[i] = (10/(2**numC-1))*auxConv2

            if (sinal_X[i] == 1):
                real_X[i] = real_X[i]*-1
            if (sinal_Y[i] == 1):
                real_Y[i] = real_Y[i]*-1
            if (Count > 0):
                real_X[numP-1] = melhor_X
                real_Y[numP-1] = melhor_Y

def animate(popX, popY, interval: int = 200):
    gensX = popX
    gensY = popY
    fig = plt.figure(1)
    ax = plt.axes(xlim=[-10, 10], ylim=[-10, 10])

    x = [x for x in gensX[0]]
    y = [y for y in gensY[0]]
    scatter = ax.scatter(x, y)

    def update(i):
        xy = [[dupla[0], dupla[1]] for dupla in zip(gensX[i], gensY[i])]

        scatter.set_offsets(xy)
        fig.suptitle("Generation: "+str(i))

        return scatter,

    anim = FuncAnimation(fig, update, frames=len(gensX)-1, interval=interval)
    plt.show()