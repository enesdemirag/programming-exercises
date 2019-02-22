### Answer - Inverse Factorial

We create a loop counting from one to infinite. And in every loop we check that if number can be divided without remainder and multiply the products until we reach to input value.

Here is a solution using Python.

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

Here is a solution using MATLAB.

```matlab
function output = reverse_fact(input)
% Inverse Factorial Function
    prod = 1;
    i = 1;
    while(true)
        if(mod(input, i) == 0) % If divided without remainder
            prod = prod * i;
            if(prod == input)
                break; % Exit loop
            end
        else
            i = 0;
            break;
        end
        i = i + 1;
    end
    output = i;
end
```

_Go to [question](https://github.com/enesdemirag/programming-exercises/blob/master/questions/inverse-factorial.md)._
