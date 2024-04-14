"""
Use Qiskit to write a code for Grover’s algorithm that searches for the states of a two-qubit circuit, which are 00, 01, 10, and 11. Example: if the target state is 00, then the results should be 00:1024, which means that for all the 1024 executions of the circuit, the result is always 00.  The oracle should target all the states.  Measure the circuit.  Print the circuit.  Print the results.  Plot the results. 
"""

# Grover's Algorithm
from qiskit import QuantumCircuit, Aer, execute 
from qiskit.visualization import plot_histogram
# Define the oracle that marks the solution
def oracle(circuit):
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])

#Define the diffusion operator
def diffusion(circuit):
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])
    circuit.h([0, 1])
    
#Create the quantum circuit 
circuit= QuantumCircuit(2, 2)
#Apply Hadamard gates to both qubits
circuit.h([0, 1])
#Apply Grover's algorithm for a certain number of iterations
iterations = 1
for _ in range(iterations):
    oracle(circuit)
    diffusion(circuit)
#Measure the qubits
circuit.measure([0, 1], [0, 1])
print(circuit)

#Simulate the circuit
simulator = Aer.get_backend('qasm_simulator') 
job = execute(circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts(circuit)

# Print the measurement results
print(counts)
plot_histogram(counts)
