from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

print('hello world')

Model()

# Make a simple model of binding of A and B to form a heterodimer A % B
Monomer('A', ['b'])
Monomer('B', ['a'])

Parameter('A_init', 100)
Parameter('B_init', 80)

Initial(A(b=None), A_init)
Initial(B(a=None), B_init)

Parameter('kf_AB', 0.01)
Parameter('kr_AB', 0.1)

Rule('A_binds_B', A(b=None) + B(a=None) | A(b=1) % B(a=1), kf_AB, kr_AB)

Observable('A_free', A(b=None))
Observable('B_free', B(a=None))
Observable('AB_complex', A(b=1) % B(a=1))

print(model)

# Run a simulation
tspan = np.linspace(0, 1, 101)
sim = ScipyOdeSimulator(model, tspan, verbose=True)
output = sim.run()

plt.figure(constrained_layout=True)
plt.plot(tspan, output.observables['A_free'], lw=2, label='A_free')
plt.plot(tspan, output.observables['B_free'], lw=2, label='B_free')
plt.plot(tspan, output.observables['AB_complex'], lw=2, label='AB_complex')
plt.xlabel('time')
plt.ylabel('concentration')
plt.legend(loc='best')

plt.show()
