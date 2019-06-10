import numpy as np
from networkGrowing import *
from dists import *

class Condensete(boseEinteinNetwork):
    def __init__(self, N, beta, m,trials, fitnessDistribution, keys):
        if fitnessDistribution=='FGR1':fitnessDistribution = fitGetRicher
        elif fitnessDistribution=='FGR2': fitnessDistribution = pareto
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
            Z += np.exp(np.log(i[1])) * self.degreeList[i[0]]
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
        mu2 = []
        kmax = []
        kmax2 = []
        for i in temperatures:
            if 'beta' in keys:
                keys['beta'] = 1/i
            condensate = Condensete(N=N, beta=1/i,  m=m, trials=trials, fitnessDistribution=fitnessDistribution, keys=keys)
            aux_mu, aux_kmax = condensate.getChemicalPotencial_and_maxK()
            mu.append(aux_mu)
            mu2.append(aux_mu**2)
            kmax.append(aux_kmax)
            kmax2.append(aux_kmax**2)
            print(i)
        mu = np.array(mu)/trials
        mu2 = np.array(mu2)/trials
        kmax = np.array(kmax)/trials
        kmax2 = np.array(kmax2)/trials
        return np.array(temperatures), mu, kmax, np.sqrt(mu2-mu**2), np.sqrt(kmax2 - kmax**2)

    @staticmethod
    def getLambdaTBE(N, m , trials):
        fitnessDistribution = pareto
        keys = {'lamb':0}
        lamb = np.arange(0.5, 1.5, 0.01)
        kmax = []
        kmax2 = []
        mu = []
        mu2 = []
        for i in lamb:
            keys['lamb'] = i
            condensate = Condensete(N=N, beta=1,  m=m, trials=trials, fitnessDistribution=fitnessDistribution, keys=keys)
            aux_mu, aux_kmax = condensate.getChemicalPotencial_and_maxK()
            mu.append(aux_mu)
            mu2.append(aux_mu**2)
            kmax.append(aux_kmax)
            kmax2.append(aux_kmax**2)
            print(i)
        return np.array(lamb), np.array(mu), np.array(kmax), np.array(mu2), np.array(kmax2)







