import numpy as np
import igraph as ig
import matplotlib.pyplot as plt

class boseEinteinNetwork():
    def __init__(self, m, fitnessDistribution, keys):
        self.n = m
        self.K = {}
        self.keys = keys
        self.__m = m
        self.__time = 0
        self.__fitnessDistribution = fitnessDistribution
        self.__networkInicialization()
        self.__indexArray = [i for i in range(self.n)]

    def __networkInicialization(self):
        self.__createFitnessList()
        self.__createDegreeList()
        self.__createEdgeList()
        self.__createK()
        self.__time = self.__m

    def __createFitnessList(self):
        self.fitnessList = np.array([ self.__fitnessDistribution(**self.keys) for i in range(self.n)])

    def __createDegreeList(self):
        self.degreeList = np.array([self.__m for i in range(self.n)])

    def __createEdgeList(self):
        self.edgeList = set()
        for i in range(self.__m):
            for j in range(self.__m):
                if i!=j:
                    if (i,j) in self.edgeList or (j,i)  in self.edgeList:
                        pass
                    else: 
                        self.edgeList.add((i,j))

    def __createK(self):
        for i in range(self.__m):
            self.K.update({i:self.fitnessList[i]})

    def getLinkProbabilityList(self):
        return (self.degreeList * self.fitnessList)/self.getNormalization()

    def getNormalization(self):
        return np.sum(self.degreeList * self.fitnessList)

    def getFitnessDistribution(self):
        return self.__fitnessDistribution
    
    def getDistributionsKeys(self):
        return self.__keys

    def get_m(self):
        return self.__m

    def __atualizeEdgeList(self, targets):
        for i in targets:
            self.edgeList.add((self.n, i))

    def __atualizeDegreeList(self, targets):
        self.degreeList = np.append(self.degreeList, self.__m)
        for i in range(self.__m):
            self.degreeList[targets[i]] += 1

    def __atualizeK(self):
        fitness = self.fitnessList[-1]
        self.K.update({self.n :fitness})

    def newNode(self):
        linkProb = self.getLinkProbabilityList()

        targets = np.random.choice(self.__indexArray, size=self.__m, p=linkProb, replace=False)
        self.__atualizeDegreeList(targets)
        self.__atualizeEdgeList(targets)
        self.__atualizeK()

        self.fitnessList = np.append(self.fitnessList, self.__fitnessDistribution(**self.keys))
        self.__indexArray.append(self.n)

        self.n += 1
        self.__time += 1

    def addNodes(self, N):
        for i in range(N-1):
            self.newNode()

   








