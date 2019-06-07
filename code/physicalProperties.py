import numpy as np
from networkGrowing import *
from dists import *

class Condensete(boseEinteinNetwork):
    def __init__(self, N, beta, m,trials, fitnessDistribution, keys):
        if fitnessDistribution=='FGR':fitnessDistribution = fitGetRicher
        elif fitnessDistribution=='FGA': fitnessDistribution = scaleFree
        else: pass 
        super(Condensete, self).__init__(m, fitnessDistribution, keys)
        self.beta = beta 
        self.addNodes(N-1)
        self.trials = trials
        self.N = N

    def energyLevels(self):
        return self.__eta2energy(self.fitnessList)  

    def partitionFunctio(self):
        Z = 0
        for i in self.K.items():
            Z += np.exp(-self.beta * 1/self.beta * np.log(i[1])) * self.degreeList[i[0]]
        return Z

    def meanValues(self):
        meanZ = 0
        meanMaxK = 0
        for i in range(self.trials):
            newNetwork = Condensete( self.N, self.beta, self.get_m(), self.trials, self.getFitnessDistribution(), self.keys)
            meanZ += newNetwork.partitionFunctio()
            meanMaxK += np.max(newNetwork.degreeList)

        return meanZ/self.trials, meanMaxK/self.trials

    def getChemicalPotencial_and_maxK(self):
        meanZ, meanMaxK = self.meanValues()
        m = self.get_m()
        return np.abs(-1/self.beta * np.log(meanZ/(m *self.N))), meanMaxK/(m*self.N)

    @staticmethod
    def getThermodynamics(N, m, trials, fitnessDistribution, keys, temperatures=None): 
        if type(temperatures) ==  type(None):
            temperatures = np.arange(0.1, 3, 0.1)
        mu = []
        maxK = []
        for i in temperatures:
            keys['beta'] = 1/i
            condensate = Condensete(N=N, beta=1/i,  m=m, trials=trials, fitnessDistribution=fitnessDistribution, keys=keys)
            aux_mu, aux_maxK = condensate.getChemicalPotencial_and_maxK()
            mu.append(aux_mu)
            maxK.append(aux_maxK)
            print(i)
        return np.array(temperatures), np.array(mu), np.array(maxK)





