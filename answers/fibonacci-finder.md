### Answer - Fibonacci Finder

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
end```

_Go to [question](https://github.com/enesdemirag/programming-exercises/blob/master/questions/fibonacci-finder.md)._
