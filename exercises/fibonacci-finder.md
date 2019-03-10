### Theoretical - Fibonacci Finder

The Fibonacci sequence is one of the most famous formulas in mathematics. Each number in the sequence is the sum of the two numbers that precede it. So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

It's true that the Fibonacci sequence is tightly connected to what's now known as the *[golden ratio](https://www.mathsisfun.com/numbers/golden-ratio.html)*, but it's topic for another exercise.  

In computer programming, Fibonacci numbers give a model for designing *[recursive programming algorithms](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Recursions/recursions.html)*. An example recursive fibonacci sequence function shown below using Python.  

```python
fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
```

For more information check out _[this](http://mathworld.wolfram.com/FibonacciNumber.html)_ website and *[wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)* page.

### Practical - Fibonacci Finder

Write a function that determines a number if its Fibonacci is given.

Example:
```
input         : 89
output        : 10
```

Here is a function which returns the index of the input number in fibonacci sequence. If input value is not a member of fibonacci sequence it gives -1.

```matlab
function output = fibonacci_finder(input)
% Fibonacci Finder: Program that determines a number if its Fibonacci is given.
    a = 0;
    b = 1;
    temp = 0;
    count = 0;
    while(true)
        temp = a;
        a = b;
        b = temp + b;
        if(a == input) % If
            break;
        end
        else if(a > input) % If input number didn't within the sequence
            count = -1; % Return -1
            break;
        end
        count = count + 1;
    end
    output = count; % Index in sequence
end
```
