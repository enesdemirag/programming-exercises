### Answer 1
```python
def inverse_fact(input):
    prod = 1
    i = 1
    while True:
        if input % i == 0:
            prod *= i
            if prod == input:
                return i
        else:
            return 0
        i += 1
```

### Answer 2
```python
def encrypt(text, shift):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(text, shift):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
    return cipher
```

### Answer 3
