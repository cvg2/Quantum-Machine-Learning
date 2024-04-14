"""
Use Pennylane to implement a QAOA to solve the minimum vertex cover problem. The goal is to find the smallest set of vertices such that each edge of the graph is linked to at least one vertex in the set. Use the graph that is used in in class exercise 1 for the QAOA topic. that is uploaded in in class exercise folder in Blackboard. The implementation should have the following details:  1. Import necessary libraries:  2. Define the number of nodes and adjacency matrix:  3. Create a graph:  4. Define the QAOA layers  5. Build the QAOA circuit  6. Define the cost function  7. Optimize the parameters  8. Run the optimization and print the results  Please refer to the a ached implementa on details of the QAOA for Minimum Vertex Cover Problem.pdf for more details to implement this exercise 1.  
"""

import numpy as np
import pennylane as qml
from pennylane import qaoa
from pennylane.optimize import GradientDescentOptimizer
import networkx as nx

# Define the number of nodes and adjacency matrix
num_nodes = 4  # replace with your actual number of nodes
adj_matrix = np.array([
    [0.0, 1.0, 1.0, 0.0],
    [1.0, 0.0, 1.0, 1.0],
    [1.0, 1.0, 0.0, 1.0], 
    [0.0, 1.0, 1.0, 0.0]
])  # replace with your actual adjacency matrix

# Create a graph
graph = nx.Graph(adj_matrix)

# Define the QAOA layers
def qaoa_layer(gamma, alpha):
    qaoa.cost_layer(gamma, hamiltonian)
    qaoa.mixer_layer(alpha, hamiltonian)

def circuit(params, **kwargs):
    qml.templates.BasicEntanglerLayers(params, wires=range(num_nodes))
    qaoa_layer(*params)

# Define the cost function
def cost_function(params):
    dev = qml.device("lightning.qubit", wires=num_nodes)
    circuit(params)
    return qml.expval(hamiltonian)

obs_list = []
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if w[i, j] != 0:
            obs_list.append(qml.PauliZ(i) @ qml.Identity(j))
hamiltonian = qml.Hamiltonian(coeffs=[-1] * len(obs_list), observables=obs_list)


# Optimize the parameters
optimizer = GradientDescentOptimizer()
params = np.random.rand(2,num_nodes)

# Run the optimization
steps = 100
for i in range(steps):
    params = optimizer.step(cost_function, params)

# Display the results
print("Optimal gamma and beta:", params)
