import numpy as np
import igraph as ig
import matplotlib.pyplot as plt

class boseEinteinNetwork():
    def __init__(self, m, fitnessDistribution):
        self.n = m
        self.K = {}
        self.__m = m
        self.__time = 0
        self.__fitnessDistribution = fitnessDistribution
        self.__networkInicialization()
        self.__indexArray = [i for i in range(self.n)]

    def __networkInicialization(self):
        self.__createFitnessList()
        self.__createDegreeList()
        self.__createAdjacency()
        self.__createK()
        self.__time = self.__m

    def __createFitnessList(self):
        self.fitnessList = np.array([ self.__fitnessDistribution() for i in range(self.n)])

    def __createDegreeList(self):
        self.degreeList = np.array([self.__m for i in range(self.n)])

    def __createAdjacency(self):
        self.adjacency = [[] for i in range(self.n + 1)]
        for i in range(self.n + 1):
            for j in range(self.n + 1):
                if j != i: self.adjacency[i].append(j)
                else: continue

    def __createK(self):
        for i in range(self.__m):
            self.K.update({i:[self.fitnessList[i], i]})

    def getLinkProbabilityList(self):
        return (self.degreeList * self.fitnessList)/self.getNormalization()

    def getNormalization(self):
        return np.sum(self.degreeList * self.fitnessList)

    def __atualizeAdjancency(self, targets):
        self.adjacency.append([])
        self.adjacency[self.n].append(targets)
        for i in targets:
            self.adjacency[i].append(self.n)

    def __atualizeDegreeList(self, targets):
        self.degreeList = np.append(self.degreeList, self.__m)
        for i in range(self.__m):
            self.degreeList[targets[i]] += 1

    def __atualizeK(self):
        fitness = self.fitnessList[-1]
        self.K.update({self.n :[fitness, self.__time]})

    def newNode(self):
        linkProb = self.getLinkProbabilityList()
        self.n += 1
        self.__time += 1

        targets = np.random.choice(self.__indexArray, size=self.__m, p=linkProb)
        self.__atualizeAdjancency(targets)
        self.__atualizeDegreeList(targets)
        self.__atualizeK()

        self.fitnessList = np.append(self.fitnessList, self.__fitnessDistribution())
        self.__indexArray.append(self.n)

    def addNodes(self, N):
        for i in range(N):
            self.newNode()







