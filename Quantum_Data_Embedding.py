"""
Perform quantum data embedding for the Iris dataset. The Iris dataset is a commonly used dataset in machine learning and consists of 150 samples of iris flowers, each with four features: sepal length, sepal width, petal length, and petal width. Encode the features of the Iris dataset into a quantum state using amplitude embedding. Use load_iris() function to load the Iris dataset. 
"""

import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data  # features
y = iris.target  # labels

# Define the number of qubits required for encoding
num_qubits = X.shape[1]

# Amplitude encoding function
def amplitude_encoding(x):
    for i in range(len(x)):
        qml.RY(x[i], wires=i)

# Quantum circuit for encoding
def quantum_embedding(x):
    amplitude_encoding(x)

# Create a quantum device
dev = qml.device("default.qubit", wires=num_qubits)

# Define the quantum function
@qml.qnode(dev)
def quantum_state(x):
    quantum_embedding(x)
    return qml.state()

# Encode each data point of the Iris dataset
quantum_states = []
for i in range(len(X)):
    state = quantum_state(X[i])
    quantum_states.append(state)

# Convert quantum states to numpy array
quantum_states = np.array(quantum_states)

# Check the shape of the quantum states array
print("Shape of quantum states array:", quantum_states.shape)
