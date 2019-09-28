### Theoretical - Heat Transfer

We will use symbolic programming (sympy) instead of classical approach.
t_final = (m1c1t1 + m2c2tt2) / (m1c1 + m2c2)

### Practical - Heat Transfer

```python
class Matter(object):
    def __init__(self, mass, constant, temperature):
        self.mass = mass
        self.c = constant
        self.temp = temperature

def heatTransfer(m1, m2):  # Find equilibrium temperature
    # Q = m * c * deltaT
    q1 = m1.mass * m1.c * (m1.temp - equilibrium)
    q2 = m2.mass * m2.c * (equilibrium - m2.temp)
    q1 = q2
    return equilibrium

hot_water = Matter(6, 1, 85)
cold_water = Matter(8, 1, 10)
t_balance = heatTransfer(hot_water, cold_water)
print(t_balance)
```