### Answer - Caesar Cipher

We read every character one by one using for loop. Instead of using alphabet string I used Python's two build-in functions for shifting. ```ord()``` function converts character to its _[ascii code](https://theasciicode.com.ar)_ and the ```chr()``` function works vice-versa. Firstly we get the ascii number of the character, then add that shift value.

However, English alphabet starts from a(97) and ends at z(122) or for capitalize alphabet it's A(65) to Z(90). In order to avoid other ascii characters first we need to remove characters before 'a', then shift it. Be careful here, because after 'z' again starts different characters, so we can prevent it to exceed 26 using modulo operator. Finally we add removed characters back and convert back from ascii to the char.

```python
def encrypt(text, shift):
    cipher = ""
    for char in text:
        if char == ' ': # If it's space character add without any change
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) # 65 for 'A'
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97) # 97 for 'a'
    return cipher
```

```python
def decrypt(text, shift):
    cipher = ""
    for char in text:
        if char == ' ':
            cipher = cipher + char # If it's space character add without any change
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65) # 65 for 'A'
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97) # 97 for 'a'
    return cipher
```

---

Here is another way to write function using alphabet string.

```python
def encrypt(text, shift):
    lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_case_alphabet = lower_case_alphabet.upper() # Capitalize
    cipher = ""
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            # Find index of char in upper_case_alphabet and shift it.
            cipher = cipher + upper_case_alphabet[(upper_case_alphabet.index(char) + shift) % 26]
        else:
            # Find index of char in lower_case_alphabet and shift it.
            cipher = cipher + lower_case_alphabet[(lower_case_alphabet.index(char) + shift) % 26]
    return cipher
```

```python
def encrypt(text, shift):
    lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_case_alphabet = lower_case_alphabet.upper()
    cipher = ""
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            # Find index of char in upper_case_alphabet and shift it.
            cipher = cipher + upper_case_alphabet[(upper_case_alphabet.index(char) - shift) % 26]
        else:
            # Find index of char in lower_case_alphabet and shift it.
            cipher = cipher + lower_case_alphabet[(lower_case_alphabet.index(char) - shift) % 26]
    return cipher
```
