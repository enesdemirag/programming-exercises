### Answer - Inverse Factorial

We create a loop counting from one to infinite. And in every loop we check that if number can be divided without remainder and multiply the products until we reach to input value.

```python
def inverse_fact(input):
    prod = 1
    i = 1
    while True:
        if input % i == 0: # If divided without remainder
            prod *= i
            if prod == input:
                return i
        else:
            return 0
        i += 1
```
