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

![image](https://user-images.githubusercontent.com/70408681/134777322-b85ede72-14cd-4305-918f-cd5df285c997.png)
![image](https://user-images.githubusercontent.com/70408681/134777329-561a68b0-a9b8-4865-a8d1-ad76d8e7d7b0.png)

Where, **F** is the external force applied to the dynamic system. **m, b, and k** denotes the mass, damping coefficient, and spring coefficient. **x, x', and x''** denotes the displacement, velocity and acceleration vectors respectively.

### Mass Spring Damper Simulation

Creating a physics simulation of a Mass-Spring-Damper System and plot the displacement, velocity and acceleration changes.

For simplicity, we will use use _[matplotlib](https://matplotlib.org/)_ package to plot in order to simulate displacement, velocity and acceleration quantities. 

All we need to do is implementing **Force = mass * acceleration + b * velocity + k * position** equation. In this system lets assume external force is zero and initial position is to be entered as input.

<p align="center">
  <img src="https://cdn.kastatic.org/ka-perseus-images/6a38c2127e4ea04fadf58c016b81d19a4a46d5c0.gif">
</p>

Also we know that in order to compute position we need to take integral of acceleration two times. Because computers can't calculate real integral, we should use [limit definition of the integral](https://www.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-3/a/definite-integral-as-the-limit-of-a-riemann-sum) to approximate an integral like above.

Mass will will move from initial point (x = 15) to the center (x = 0) and oscillate. It will lose its energy in time and stop at the center after a while.


```python
from visualizer import Visualizer # Import Visualizer class

dt = 0.05 # ΔT (sampling period) seconds

# Initial values
position = Inputvalue
velocity = 0
acceleration = 0

# Constants
mass = 4.2 # mass
k = 2.1 # spring coefficient
b = 0.5 # damping coefficient

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
```

The result should be like this. You can find the full code from [here](materials/mass-spring-damper-simulation/demo.py).

<p align="center">
  <img src="images/msd-simulation.gif">
</p>

References used (for illustrations): 
1. http://www.sharetechnote.com/html/DE_Modeling_Example_SpringMass.html#SingleSpring_SimpleHarmonic_Vert_Damp 
