class Individual:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def fitnessCalc(self):
        Z = -(self.x**2 + self.y**2) + 4
        return Z

    def getFitness(self) -> float:
        return self.fitness

    def setPercentage(self, percentage) -> None:
        self.individual_percentage = percentage

    def getPercentage(self) -> None:
        return self.individual_percentage
