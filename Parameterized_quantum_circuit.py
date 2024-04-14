"""
 Implement a parameterized quantum circuit, also known as an ansatz, using PennyLane. The circuit should prepare a single-qubit state that can be expressed as a linear combination of the |0⟩ and |1⟩ states. The parametrized circuit should perform the following transformation: U(θ)=Ry (θ)⋅Rz (θ) Where Ry (θ) represents a rotation around the y-axis by an angle θ and Rz (θ) represents a rotation around the z-axis by an angle θ.  Implement the parameterized circuit using 1 qubit, and write a function that takes the angle θ as input and returns the statevector of the resulting quantum state.
"""

import pennylane as qml
from pennylane import numpy as np

def ansatz(theta):
    dev = qml.device("default.qubit", wires=1)
    
    @qml.qnode(dev)
    def circuit(theta):
        qml.RY(theta, wires=0)
        qml.RZ(theta, wires=0)
        return qml.state()

    return circuit(theta)

# Define the angle theta
theta = 0.5  # for example

# Get the statevector of the resulting quantum state
statevector = ansatz(theta)
print(statevector)
