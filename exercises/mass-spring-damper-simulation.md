### Question - Mass Spring Damper Simulation

todo

### Answer - Mass Spring Damper Simulation

```python
import numpy as np
from visualizer import Visualizer

dt = 0.05
position = 20.0
velocity = 0.0
acceleration = 0.0
mass = 1.0
k = 2.5
b = 0.3

# Callback function
def set(time):
    global dt, position, velocity, acceleration, mass, k, b

    spring_force = (k * position)
    damper_force = b * velocity

    acceleration = - spring_force / mass - damper_force / mass
    velocity += (acceleration * dt)
    position += (velocity * dt)

    return (position, 0), 0

# Create Simulation
Visualizer(callback=set, interval=dt * 1000.0, simulation_time=20.0, initial=(position, 0, velocity, 0, acceleration, 0))
```
