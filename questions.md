### Question 1 - Inverse Factorial

In mathematics, the **factorial** of a integer n, denoted by n!, is the product of all positive integers less than or equal to n.

Write a function that returns a number if its factorial is given.
If the input value does not have a solution, return 0.

Example:
```
input         : 120
output        : 5
```

### Question 2 - Caesar Cipher

**Caesar Cipher** is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the text is replaced by a letter some fixed number of positions down the alphabet.

_Alphabet : "abcdefghijklmnopqrstuvwxyz"_

Write encrypt and decrypt functions for Caesar Cipher Encryption.

Example:
```
input         : "hello", 5
output        : "mjqqt"
```

```
input         : "Oazsdmfgxmfuaze", 12
output        : "Congratulations"
```

You can watch this _[Khan Academy Video](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher)_ and read this _[article](http://www.cs.trincoll.edu/~crypto/historical/caesar.html)_ for more information.

### Question 3 - Image Processing

An **image kernel** is a small matrix used to apply effects such as blurring, sharpening, and edge detection. They are like ancestors of modern image processing techniques and even used today in machine learning for _feature extraction_, a technique for determining the most important portions of an image.

Below matrix is a 3x3 blur kernel. For each pixel in the image, we take 3x3 block of neighbor pixels and multiply each pixel by the corresponding entry of the kernel and then take the sum. That sum becomes a new value of the pixel.

<table align = center>
    <caption>3x3 Gaussian Blur Kernel</caption>
    <tr>
        <td align = center>0.0625</td>
        <td align = center>0.125</td>
        <td align = center>0.0625</td>
    </tr>
    <tr>
        <td align = center>0.125</td>
        <td align = center>0.25</td>
        <td align = center>0.125</td>
    </tr>
    <tr>
        <td align = center>0.0625</td>
        <td align = center>0.125</td>
        <td align = center>0.0625</td>
    </tr>
</table>

Write a function that can apply the entered kernel to an image. You can use image *[here](materials/question3-image-processing)*.

Example:
```
input   : (image in a matrix form), [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
output  : (filtered image in a matrix form)
```

If you want to learn more about image kernels, you can check *[wikipedia](https://en.wikipedia.org/wiki/Kernel_(image_processing)* page and _[this documentation](https://docs.gimp.org/en/gimp-filter-convolution-matrix.html)_ from gimp, also I certainly suggest you to look at _[this website](http://setosa.io/ev/image-kernels/)_ for visually explanation of image kernels.
