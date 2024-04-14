"""
The gates available in Qiskit are only small part of quantum gates one can apply in quantum circuits. In this exercise, create the following gate and apply on a one qubit system using the operator method in qiskit. Also provide the screenshot of the Python code 
"""

from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.quantum_info import Operator
import numpy as np

custom_matrix = np.array([[0, (1-1j)/np.sqrt(2)],
                          [(1+1j)/np.sqrt(2), 0]])

unitary_op = Operator(custom_matrix)

qc = QuantumCircuit(1)

qc.append(unitary_op, [0])

print(qc)


"""
Show using the unitary simulator in Qiskit that the following two circuits are equivalent. Tip: You can show that they are equivalent using the difference in their unitary. Also provide the screenshot of the Python code 

"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

qc1 = QuantumCircuit(3)
qc1.cx(0, 2)

qc2 = QuantumCircuit(3)
qc2.cx(0, 1)
qc2.cx(1, 2)
qc2.cx(0, 1)
qc2.cx(1, 2)

op1 = Operator(qc1)
op2 = Operator(qc2)


diff_op = op1 - op2

print(diff_op)
# The difference needs to be 0 for both circuits to be equivalent

"""
Using Python code, perform the following Tensor operators.
"""

import numpy as np

u = np.array([-2, -1, 0, 1])
v = np.array([1, 2, 3])

TP_uv = np.tensordot(u, v, axes = 0)
TP_vu = np.tensordot(v, u, axes = 0)

print("u ⊗ v =", TP_uv)
print("v ⊗ u =", TP_vu)
