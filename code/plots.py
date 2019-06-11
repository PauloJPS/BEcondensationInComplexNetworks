import numpy as np
import matplotlib.pyplot as plt
import igraph as ig
import networkx as nx 
from igraph2nx import *
from dists import *
from physicalProperties import *


def nets():
    k = {'theta':1, 'beta':1}
    c = Condensete(1000, 5, 2, 1, 'FGR1', k)

def plotPhaseTransitions():

    t = np.loadtxt('data/t_N_5000_m_2_tri_50_theta_1')
    mu = 20*np.loadtxt('data/mu_N_5000_m_2_tri_50_theta_1')
    mu2 = 20*np.loadtxt('data/mu_N_5000_m_2_tri_50_theta_1')
    k = 20*np.loadtxt('data/k_N_5000_m_2_tri_50_theta_1')
    k2 = 20*np.loadtxt('data/k_N_5000_m_2_tri_50_theta_1')

    t1 = np.loadtxt('data/t_N_1000_m_2_tri_50_theta_1')
    mu1 = np.loadtxt('data/mu_N_1000_m_2_tri_50_theta_1')
    mu21 = np.loadtxt('data/mu_N_1000_m_2_tri_50_theta_1')
    k1 = np.loadtxt('data/k_N_1000_m_2_tri_50_theta_1')
    k21 = np.loadtxt('data/k_N_1000_m_2_tri_50_theta_1')

    t2 = np.loadtxt('data/t_N_10000_m_2_tri_50_theta_1')
    mu2 = np.loadtxt('data/mu_N_10000_m_2_tri_50_theta_1')
    mu22 = np.loadtxt('data/mu_N_10000_m_2_tri_50_theta_1')
    k2 = np.loadtxt('data/k_N_10000_m_2_tri_50_theta_1')
    k22 = np.loadtxt('data/k_N_10000_m_2_tri_50_theta_1')


    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(13, 10))

    ax[0].scatter(t1[1:], mu1[1:], marker='^', label=r'$T=5\times10^3$', s=70, c='red', edgecolor='black')
    ax[0].scatter(t2[1:], mu2[1:], marker='*', label=r'$T=5\times10^4$', s=70, c='blue', edgecolor='black')
    ax[0].scatter(t[1:], mu[1:], marker='o', label=r'$T=10^3$', s=70, c='green', edgecolor='black')

    ax[1].scatter(t1[1:], k1[1:], marker='o', s=70, c='green', edgecolor='black')
    ax[1].scatter(t2[1:], k2[1:], marker='*', s=70, c='blue', edgecolor='black')
    ax[1].scatter(t[1:], k[1:], marker='^', s=70, c='red', edgecolor='black')
 
    
    ax[0].plot([0.906, 0.906], [0.00001, 10], color='black')
    ax[1].plot([0.906, 0.906], [0.0001, 10], color='black')

    ax[1].set_xlabel('T', fontsize=20)
    ax[0].set_ylabel(r'$|\mu|$', fontsize=30, labelpad=30, rotation=0)
    ax[1].set_ylabel(r'$\frac{K_{max}}{mt}$', fontsize=30, labelpad=30, rotation=0)
    
    ax[1].set_xscale('log')
    ax[0].set_yscale('log')
    ax[1].set_yscale('log')

    #ax[1].set_xlim((0.0, 3))
    ax[0].set_ylim((5e-5, 5))
    ax[1].set_ylim((10e-3, 5))
    
    ax[0].text(1.3, 0.01, r"$FGR$", fontsize=30)
    ax[0].text(0.5, 0.01, r"$BE$", fontsize=30)

    ax[1].text(1.3, 0.3, r"$FGR$", fontsize=30)
    ax[1].text(0.5, 0.5, r"$BE$", fontsize=30)

    ax[1].arrow(0.6, 0.035, 0.27, -0.022, 
            shape='full', head_width=0.005,head_length=0.02, color='black')
    ax[1].text(0.53, 0.035, r'$T_{C}$', fontsize=20)

    plt.tight_layout(pad=1.3)

    ax[0].legend(fontsize=20)


def plotRhoHist():
    ensamble = []
    rho = lambda x : 2*(-np.log(x))/x
    for i in range(1000):
        ensamble.append(fitGetRicher(1,1))
    x = np.arange(np.exp(-1), 1, 0.01)

    plt.figure(figsize=(13,10))
    plt.hist(ensamble, density=1, label=r'$F^{-1}(u)$', color='green', rwidth=0.9)
    plt.plot(x, rho(x), label=r'$\rho(\eta)$', color='red', lw=5)

    plt.legend(fontsize=20)
    plt.xlabel(r'$\eta$', fontsize=30, labelpad=10)
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


