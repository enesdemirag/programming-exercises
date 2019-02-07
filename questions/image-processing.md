### Question - Image Processing

An **image kernel** is a small matrix used to apply effects such as blurring, sharpening, and edge detection. They are like ancestors of modern image processing techniques and even used today in machine learning for _feature extraction_, a technique for determining the most important portions of an image.

Below matrix is a 3x3 Gaussian Blur Kernel. For each pixel in the image, we take 3x3 block of neighbor pixels and multiply each pixel by the corresponding entry of the kernel and then take the sum. That sum becomes a new value of the pixel.

<table align = center>
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

Write a function that can apply the entered kernel to an image. You can use image *[here](materials/image-processing)*.

Example:
```
input   : (image in a matrix form), [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
output  : (filtered image in a matrix form)
```

If you want to learn more about image kernels, you can check *[wikipedia](https://bit.ly/2yfaapD)* page and _[this documentation](https://docs.gimp.org/en/gimp-filter-convolution-matrix.html)_ from gimp, also I certainly suggest you to look at _[this website](http://setosa.io/ev/image-kernels/)_ for visually explanation of image kernels.
