import numpy as np
import matplotlib.pyplot as plt
import igraph as ig
import networkx as nx 
from igraph2nx import *

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


