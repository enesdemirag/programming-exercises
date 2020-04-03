import numpy as np
from scipy.integrate import odeint # For differential calculations
import matplotlib.pyplot as plt # For visualization

# Coronavirus Spread Mathematical Model

# In SIR Model we split the total population into three groups.
# S = Suspectibles (People who could potantically catch the virus)
# I = Infectives (People currently have the virus and can infect others)
# R = Recovered / Removed (People who already caught the virus, then either recovered or died, and cannot infect others)

# Lets define initial conditions

N = 1000             # Total population
max_time = 15       # Simulation time

Si = N * 0.99       # Normal people
Ii = N - Si         # Infected people
Ri = 0

# S + I + R should always be equal to N

transmission_rate = 4.2
recovery_rate = 0.9
t = np.linspace(0, max_time - 1, max_time * 100) # x-axis

# The SIR model differential equations
def model(z, t):
    (S, I, R) = z
    dsdt = -(transmission_rate * S * I) / N
    didt = (transmission_rate * S * I) / N - (recovery_rate * I)
    drdt = (recovery_rate * I)
    return (dsdt, didt, drdt)

initial_vals = (Si, Ii, Ri) # initial values vector

S, I, R = odeint(model, initial_vals, t).T

fig = plt.figure(1)
ax1 = fig.add_subplot(211)
ax1.plot(t, S, 'b', label='Suspectibles')
ax1.plot(t, I, 'r', label='Infectives')
ax1.plot(t, R, 'g', label='Recovered')
ax1.set_xlabel('Time')
ax1.set_ylabel('Population')
legend = ax1.legend()

###

transmission_rate = 2.2
recovery_rate = 0.9

# The SIR model differential equations

initial_vals = (Si, Ii, Ri) # initial values vector

S, I, R = odeint(model, initial_vals, t).T

ax2 = fig.add_subplot(212)
ax2.plot(t, S, 'b', label='Suspectibles')
ax2.plot(t, I, 'r', label='Infectives')
ax2.plot(t, R, 'g', label='Recovered')
ax2.set_xlabel('Time')
ax2.set_ylabel('Population')
legend = ax2.legend()

plt.show()