"""
Find the minimum Eigenvalue of the Hamiltonian H = Z ⊗ Z where is the Z‐Pauli operator
"""
from qiskit.circuit.library import EfficientSU2
from qiskit_algorithms.minimum_eigensolvers import VQE 
from qiskit_algorithms.optimizers import SPSA
from qiskit_aer.primitives import Estimator as AerEstimator
from qiskit.quantum_info import Pauli


aer_estimator = AerEstimator(run_options={"shots": 2048, "seed": 42})
opt = SPSA(maxiter=50)
ansatz = EfficientSU2(2, reps=1)

print(ansatz)

vqe = VQE(aer_estimator, ansatz, opt)
Z = Pauli('Z')
hamiltonian = Z^Z

result = vqe.compute_minimum_eigenvalue(hamiltonian)
 
print(result.eigenvalue)
