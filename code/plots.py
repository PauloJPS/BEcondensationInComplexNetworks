import numpy as np
import matplotlib.pyplot as plt
import igraph as ig
import networkx as nx 
from igraph2nx import *
from dists import *


def plotPhaseTransitions():

    t = np.loadtxt('data/t_N_1000_m_2_tri_500_theta_2')
    mu = np.loadtxt('data/mu_N_1000_m_2_tri_500_theta_2')
    k = np.loadtxt('data/k_N_1000_m_2_tri_500_theta_2')

    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(16,9))
    ax[0].scatter(t, mu, alpha=0.6, c='black')
    ax[1].scatter(t, k, alpha=0.6, c ='black')
    
    ax[0].plot([0.74, 0.74], [0.1, 10], color='black')
    ax[1].plot([0.74, 0.74], [0.0001, 10], color='black')

    ax[1].set_xlabel('T', fontsize=20)
    ax[0].set_ylabel(r'$|\mu|$', fontsize=30, labelpad=30, rotation=0)
    ax[1].set_ylabel(r'$K_{max}/mt$', fontsize=30)
    
    ax[1].set_xscale('log')
    ax[0].set_yscale('log')
    ax[1].set_yscale('log')

    ax[1].set_xlim((0.001, 10))
    ax[1].set_ylim((0.001, 5))
    ax[0].set_ylim((0.5, 5))

    ax[0].text(1.3, 0.8, r"$FGR$", fontsize=30)
    ax[0].text(0.05, 2.5, r"$BE$", fontsize=30)

    ax[1].text(1.3, 0.8, r"$FGR$", fontsize=30)
    ax[1].text(0.04, 0.01, r"$BE$", fontsize=30)

    plt.tight_layout(pad=1.3) 

def plotRhoHist():
    ensamble = []
    rho = lambda x : 2*(-np.log(x))/x
    for i in range(1000):
        ensamble.append(rhoEta(1,1))
    x = np.arange(np.exp(-1), 1, 0.01)

    plt.figure(figsize=(13,10))
    plt.plot(x, rho(x), label=r'$\rho(\eta)$')
    plt.hist(ensamble, density=1, label=r'$F^{-1}(u)$')

    plt.legend(fontsize=20)
    plt.xlabel(r'$\eta$', fontsize=30, labelpad=-10)
    plt.ylabel('Freq.', rotation=0, labelpad=35, fontsize=20)
    #plt.tight_layout()




def plotER_and_BA():
    er = ig.Graph.Erdos_Renyi(500, 0.01)
    erlayout = er.layout_auto().coords

    ba = ig.Graph.Barabasi(500, 1)
    balayout = ba.layout_auto().coords

    fig, ax = plt.subplots(2,2, figsize=(16, 9))
    
    ernx = ig2nx(er)
    banx = ig2nx(ba)

    nx.draw_networkx_nodes(ernx, erlayout, ax=ax[0][0], node_size=10)
    nx.draw_networkx_edges(ernx, erlayout, ax=ax[0][0],alpha=0.1)
    
    nx.draw_networkx_nodes(banx, balayout, ax=ax[0][1], node_size=10)
    nx.draw_networkx_edges(banx, balayout, ax=ax[0][1], alpha=0.1)

    ax[0][0].axis('off')
    ax[0][1].axis('off')

    ax[0][0].set_title('Erdos-Renyì', fontsize=20)
    ax[0][1].set_title('Barabasi-Albert', fontsize=20)

    ax[1][0].set_title('Dist. de Grau ER', fontsize=20)
    ax[1][1].set_title('Dist. Grau BA', fontsize=20)



    ax[1][0].hist(er.degree())
    ax[1][1].hist(ba.degree())

    ax[1][1].set_yscale('log')
    ax[1][1].set_xscale('log')
    

    plt.tight_layout()


