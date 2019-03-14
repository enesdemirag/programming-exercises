### Theoretical - Mass Spring Damper Simulation

Mass-Spring-Damper System would be the most common and most important example as the same time in differential equation. Especially you are studying mechanical or control engineering, you would be very familiar with this kind of model.

_The sum of the forces acting on a body equal its mass times it’s acceleration. - Newtons 2nd Law_

The **mass** of the dynamic system is lumped into a single point mass in the system. The inertial effect of the dynamic system is related through this lumped mass.

The stored energy of the dynamic system is modelled as a one-dimensional **spring** in the system. The spring is able to store energy inside when it is stretched or compressed from its original length.

The consumed energy of the dynamic system is modelled through a one-dimensional **damper** in the system. You can think that it is able to waste energy as heat in the dynamic system.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Mass-Spring-Damper.png" width="382" height="224">
</p>

These three components, **mass, spring and damper** can model any dynamic response situation in a general sense. Mathematically the linear dynamic equation is represented below.

<p align="center">
  <img src="http://bodetechnics.com/wp-content/uploads/2018/01/free_body_diagram_short_form.jpg">
</p>

Where, **F** is the external force applied to the dynamic system. **m, b, and k** denotes the mass, damping coefficient, and spring coefficient. **x, x', and x''** denotes the displacement, velocity and acceleration vectors respectively.

For more information, you can check [this website](http://www.sharetechnote.com/html/DE_Modeling_Example_SpringMass.html) and [this presentation](www.sharetechnote.com/html/DE_Modeling_Example_SpringMass.html) from Prof. R.G. Longoria, University of Texas.

### Practical - Mass Spring Damper Simulation

Create a physics simulation of a Mass-Spring-Damper System and plot the displacement, velocity and acceleration changes.



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

<p align="center">
  <img src="https://uk.mathworks.com/help/examples/simscape_product/win64/ssc_mass_spring_damper_sl_02.png">
</p>
