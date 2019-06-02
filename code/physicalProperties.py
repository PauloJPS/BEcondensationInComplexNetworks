import numpy as np
from networkGrowing import *


class Condensete(boseEinteinNetwork):
    def __init__(self, N, beta, m, fitnessDistribution):
        super(Condensete, self).__init__(m, fitnessDistribution)
        self.beta = beta 
        self.addNodes(N)

    def __eta2energy(self, eta):
        return -1/self.beta * np.log(eta)

    def energyLevels(self):
        return self.__eta2energy(self.fitnessList)
    




