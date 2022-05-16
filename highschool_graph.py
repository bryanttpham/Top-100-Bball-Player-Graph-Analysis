from cProfile import label
from itertools import starmap
import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite
from networkx.algorithms.community.centrality import girvan_newman
import numpy as np
import matplotlib.pyplot as plt

print(nx.__version__)


#Read the different csv files
player = pd.read_csv('player_nodes.csv')
college = pd.read_csv('player_edges.csv')
highest = pd.read_csv('highest_node.csv')
date = pd.read_csv('highschool_date.csv')
hsranking = pd.read_csv('highschool_ranking.csv')


#Convert dataframe into list
player_array = player.values.tolist()
college_array = college.values.tolist()
highest_array = highest.values.tolist()
date_array = date.values.tolist()
hsranking_array=hsranking.values.tolist()
test = player_array[0]

B = nx.Graph()
#print(len(player_array))
#print(len(college_array))
#print(len(date_array))
#print(len(hsranking_array))

#Add nodes and edges
for x in range(0, 1873):
    currentPlayer = ' '.join(player_array[x])
    currentCollege= ' '.join(college_array[x])
    currentHighest= ' '.join(highest_array[x])
    currentDate= str(date_array[x])
    currentRanking=str(hsranking_array[x])
    # highest level: highschool accounted for in highest_array
    # Avoid having to work with different indexes 
    #avoid double counting
    #B.add_node(currentCollege,bipartite=1)
    B.add_node(currentPlayer,bipartite=0)
    B.add_node(currentHighest,bipartite=1)
    B.add_node(currentDate,bipartite=1)
    B.add_node(currentRanking,bipartite=1)
    B.add_edge(currentPlayer,currentCollege)
    B.add_edge(currentPlayer,currentHighest)
    B.add_edge(currentPlayer,currentDate)
    B.add_edge(currentPlayer,currentRanking)

#B.add_node('test',bipartite=1)
#B.add_edge('Ray Young','test')
#B.add_edge('JaRon Rush','test')




top_nodes = {n for n, d in B.nodes(data=True) if d["bipartite"] == 0}
bottom_nodes = set(B) - top_nodes
G = bipartite.projected_graph(B, bottom_nodes)

F = bipartite.projected_graph(B, ["JaRon Rush", "Ray Young"], multigraph=True)

# Given the community of good players 
# Any attribute that has int datatype is references as ['x']
#Weight: Quantity of people who share attributes
#(Attribute1,Attribute2,Weight)
#C = bipartite.weighted_projected_graph(B, ["bad"])
#C = bipartite.weighted_projected_graph(B, ["great"])
#C = bipartite.weighted_projected_graph(B, ["great"])
#C = bipartite.weighted_projected_graph(B, ["good"])
#C = bipartite.weighted_projected_graph(B, ["rookie"])
#C = bipartite.weighted_projected_graph(B, ["['unranked']"])

#C = bipartite.weighted_projected_graph(B, ["allstar"])

#prints projected bipartite graph data
#print(list(C.edges(data=True)))

options = {
    'node_size': 30,
    'width': 3
}

#test=list(nx.connected_components(G))
#print(test[0])
#print("  ")
#print(test[1])
#print("  ")
#print(test[2])
#print("  ")
#print(test[3])
#print("  ")
#print(test[4])
nx.draw(G,with_labels=True, **options)

plt.show()
 