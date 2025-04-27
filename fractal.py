import numpy as np
import matplotlib.pyplot as plt

# 1. Decoherence error for qubit
theta = np.linspace(0, np.pi, 100)
delta = np.sin(theta)**2  # Simplified model
plt.plot(theta, delta)
plt.xlabel("Superposition angle θ")
plt.ylabel("δ(ρ)")
plt.title("Quantum-Classical Gap")

# 2. Fixed-point error
rho = np.linspace(0, 1, 100)  # Mixing parameter
error = np.abs(rho - (1 - rho))  # For g = σz
plt.plot(rho, error)
plt.xlabel("State ρ")
plt.ylabel("‖g(ρ) - ρ‖")

# 3. Surjectivity defect vs dimension
d = np.arange(2, 10)
delta_d = 1 - 1/np.sqrt(d)
plt.plot(d, delta_d, 'o-')
plt.xlabel("Dimension d")
plt.ylabel("δ(d)")