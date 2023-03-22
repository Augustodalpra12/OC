# Desenvolver uma solução de Otimização Combinatória
# com abordagem de um Algoritmo Genético
# Codificação: Binária      Seleção: Roleta
# Cruzamento: Dois Pontos   Mutação: Binária
# Elitismo: 1 indivíduo por Geração

# Função de Otimização: 𝑍 = −(𝑥² + y²) +4
# Restrições:    x ∈ [-10, 10] && y ∈ [-10, 10]
# Imports
import numpy
import random
from Individual import Individual
from func import *
#==============================Condições=====================================#
cromossomos = 30
pC = 0.75
pM = 0.025
pop_size = int(input("Population size: "))
genCount = 0
generations = int(input("Generaion times: "))
#=======================Gerando a Primeira População=========================#
pop = numpy.zeros((pop_size, cromossomos))
initPop(pop, pop_size, cromossomos)
pop2 = numpy.zeros((pop_size, cromossomos))
initPop(pop2, pop_size, cromossomos)
#======================Algumas variaveis=====================================#
indX = numpy.zeros(cromossomos)
indY = numpy.zeros(cromossomos)
realX = numpy.zeros(pop_size)
realY = numpy.zeros(pop_size)
bestRealX = numpy.zeros(1)
bestRealY = numpy.zeros(1)
sinalX = numpy.zeros(pop_size)
sinalY = numpy.zeros(pop_size)
fit = numpy.zeros(pop_size)
fitReal = numpy.zeros(pop_size)
newGenX = numpy.zeros((pop_size, cromossomos))
newGenY = numpy.zeros((pop_size, cromossomos))
bestIndX = numpy.zeros(cromossomos)
bestIndY = numpy.zeros(cromossomos)
x_pop = numpy.zeros((generations+1, pop_size))
y_pop = numpy.zeros((generations+1, pop_size))
fit_pop = numpy.zeros((generations+1, pop_size))
#======================Começçççççççççççççççççççççççççççooou=================#


while (genCount <= generations):
    newInds = 0
    newInds2 = 0
    aux_size = 1
    while (newInds < (pop_size-aux_size)):
        if (genCount > 0):
            pop[pop_size-1] = bestIndX[:]
            pop2[pop_size-1] = bestIndY[:]

# =======Binario para decimal
        binToDec(pop, pop2, bestRealX, bestRealY, sinalX, sinalY,
        realX, realY, genCount, cromossomos, pop_size)

        # =======Fit
        fitTotal = 0
        if (genCount > 0):
            pop[pop_size-1] = bestIndX
            pop2[pop_size-1] = bestIndY

        for i in range(pop_size):
            fit[i] = -(realX[i]**2+realY[i]**2)+4
            fit[i] = fit[i]+196
            fitTotal = fit[i]+fitTotal
    # =======Probabilidade dos homi
        probInd = numpy.zeros(pop_size)
        probTotal = numpy.zeros(pop_size)
        for i in range(pop_size):
            probInd[i] = (1/fitTotal)*fit[i]
    # =======Kassino
        for i in range(pop_size):
            if (i == 0):
                probTotal[i] = probInd[i]
            else:
                probTotal[i] = probInd[i]+probTotal[i-1]

        roletaA = random.uniform(0, 1)
        i = 0
        while (roletaA > probTotal[i]):
            i = i+1

        pai = i

        roletaB = random.uniform(0, 1)
        i = 0
        while (roletaB > probTotal[i]):
            i = i+1

        mae = i

        while (mae == pai):
            roletaB = random.uniform(0, 1)
            i = 0
            while (roletaB > probTotal[i]):
                i = i+1
            mae = i
    # =======Cruzamento de dois pontos aleatorios
        if (pC >= random.uniform(0, 1)):
            c = round(1+(cromossomos-2)*random.uniform(0, 1))
            c2 = round(1+(cromossomos-2)*random.uniform(0, 1))
            if (c2 == c):
                while (c2 == c):
                    c2 = round(1+(cromossomos-2)*random.uniform(0, 1))
            if (c > c2):
                auxc = 0
                auxc = c
                c = c2
                c2 = auxc
            gene11x = pop[pai][0:c]
            gene12x = pop[pai][c:c2]
            gene13x = pop[pai][c2:cromossomos]
            gene21x = pop[mae][0:c]
            gene22x = pop[mae][c:c2]
            gene23x = pop[mae][c2:cromossomos]
            filhox = numpy.concatenate(
                (gene11x, gene22x, gene13x), axis=None)
            filhax = numpy.concatenate(
                (gene21x, gene12x, gene23x), axis=None)

            gene11y = pop2[pai][0:c]
            gene12y = pop2[pai][c:c2]
            gene13y = pop2[pai][c2:cromossomos]
            gene21y = pop2[mae][0:c]
            gene22y = pop2[mae][c:c2]
            gene23y = pop2[mae][c2:cromossomos]
            filhoy = numpy.concatenate(
                (gene11y, gene22y, gene13y), axis=None)
            filhay = numpy.concatenate(
                (gene21y, gene12y, gene23y), axis=None)

            newGenX[newInds, :] = filhox
            newInds = newInds+1
            newGenX[newInds, :] = filhax
            newInds = newInds+1

            newGenY[newInds2, :] = filhoy
            newInds2 = newInds2+1
            newGenY[newInds2, :] = filhay
            newInds2 = newInds2+1
    # =======Mutar os monstros
            if (pM > random.uniform(0, 1)):
                m = round(1+(cromossomos-2)*random.uniform(0, 1))
                if (newGenX[newInds-2][m] == 0):
                    newGenX[newInds-2][m] == 1
                else:
                    newGenX[newInds-2][m] == 0
                if (newGenX[newInds-1][m] == 0):
                    newGenX[newInds-1][m] == 1
                else:
                    newGenX[newInds-1][m] == 0

                if (newGenY[newInds2-2][m] == 0):
                    newGenY[newInds2-2][m] == 1
                else:
                    newGenY[newInds2-2][m] == 0
                if (newGenY[newInds2-1][m] == 0):
                    newGenY[newInds2-1][m] == 1
                else:
                    newGenY[newInds2-1][m] == 0
        else:
            auxX = numpy.zeros(cromossomos)
            auxY = numpy.zeros(cromossomos)

            auxX2 = numpy.zeros(cromossomos)
            auxY2 = numpy.zeros(cromossomos)

            auxX = pop[pai, :]
            auxY = pop2[pai, :]

            auxX2 = pop[mae, :]
            auxY2 = pop2[mae, :]

            newGenX[newInds, :] = auxX
            newInds = newInds+1
            newGenX[newInds, :] = auxX2
            newInds = newInds+1

            newGenY[newInds2, :] = auxY
            newInds2 = newInds2+1
            newGenY[newInds2, :] = auxY2
            newInds2 = newInds2+1

    chad = 0
    bFit = fit[0]

    if (genCount > 0):
        binToDec(newGenX,newGenY, bestRealX, bestRealY, sinalX, sinalY,
         realX, realY, genCount, cromossomos, pop_size)

        if (genCount > 0):
            newGenX[pop_size-1] = bestIndX
            newGenY[pop_size-1] = bestIndY

        for i in range(pop_size):
            fit[i] = -(realX[i]**2+realY[i]**2)+4
            fit[i] = fit[i]+196
            fitTotal = fit[i]+fitTotal

    for p in range(pop_size):
        if (bFit < fit[p]):
            bFit = fit[p]
            chad = p

    if (genCount == 0):
        bestIndX = pop[chad, :]
        bestIndY = pop2[chad, :]
    else:
        bestIndX = newGenX[chad, :]
        bestIndY = newGenY[chad, :]

    bestRealX = realX[chad]
    bestRealY = realY[chad]

    for i in range(pop_size):
        x_pop[genCount][i] = realX[i]
        y_pop[genCount][i] = realY[i]
        fit_pop[genCount][i] = fit[i]-196

    newGenX[pop_size-1] = bestIndX[:]
    newGenY[pop_size-1] = bestIndY[:]

    elemX = realX[chad]
    elemY = realY[chad]
    print("GENERATION2 ", genCount)
    print("melhor X = ", elemX)
    print("melhor Y = ", elemY)
    print("melhor FIT = ", fit[chad]-196)
    print("==============================")

    pop = newGenX
    pop2 = newGenY
    genCount = genCount+1

animate(x_pop, y_pop, 250) 
