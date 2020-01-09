from visualizer import Visualizer # Import Visualizer class

dt = 0.05 # ΔT (sampling period) seconds

# Initial values
position = 15
velocity = 0
acceleration = 0

# Constants
mass = 1 # mass
k = 2.5 # spring coefficient
b = 0.3 # damping coefficient

# Callback Function
def set(arg):
    global dt, position, velocity, acceleration, mass, k, b # Get global variables

    spring_force = k * position # Fs = k * x
    damper_force = b * velocity # Fb = b * x'

    # If we leave the acceleration alone in equation
    # acceleration = - ((b * velocity) + (k * position)) / mass
    acceleration = - (spring_force + damper_force) / mass
    velocity += (acceleration * dt) # Integral(a) = v
    position += (velocity * dt) # Integral(v) = x

    return (position, 0) # Return position

# Start simulation
Visualizer(callback=set, interval=dt * 1000, simulation_time=30, initial=(position, 0, velocity, 0, acceleration, 0))