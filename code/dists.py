import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


def fitGetRicher(theta, beta):
    u = np.random.rand()
    return np.exp(-beta * u**(1/(theta+1)))

def pareto(lamb):
    u = np.random.rand()
    return -(u**(1/(lamb+1)) - 1)

def etaOne():
    return 1

