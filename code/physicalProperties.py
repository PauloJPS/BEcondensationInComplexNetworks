import numpy as np
from networkGrowing import *

class Condensete(boseEinteinNetwork):
    def __init__(self, N, beta, m, fitnessDistribution, trials):
        super(Condensete, self).__init__(m, fitnessDistribution)
        self.beta = beta 
        self.addNodes(N-1)
        self.trials = trials
        self.N = N

    def energyLevels(self):
        return self.__eta2energy(self.fitnessList)  
    
    def partitionFunctio(self):
        Z = 0
        for i in self.K.items():
            Z += np.exp(-self.beta * 1/self.beta * np.log(i[1][0]))
        return Z

    def meanPartitionFunction(self):
        meanZ = 0
        for i in range(self.trials):
            newNetwork = Condensete( self.N, self.beta, self.get_m(), self.getFitnessDistribution(), self.trials)
            meanZ += newNetwork.partitionFunctio()
        return meanZ/self.trials

    def getChemicalPotencial(self):
        meanZ = self.meanPartitionFunction()
        m = self.get_m()
        return -1/self.beta * np.log(meanZ /(m *self.N))

    @staticmethod
    def getThermodynamics(N, beta, m, fitnessDistribution, trials, temperatures=None): 
        temperatures = np.arange(0.1, 5, 0.1)
        mu = []
        for i in temperatures:
            condensate = Condensete(N, 1/i, m, fitnessDistribution, trials)
            mu.append(condensate.getChemicalPotencial())
            print(i)
        return np.array(temperatures), np.array(mu)




