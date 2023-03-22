import random


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