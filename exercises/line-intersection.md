### Theoretical - Line Intersection

In a 2D space, there are 3 ways how 2 lines interact with each other.

They can be parallel, which means they preserve the same distance apart every point and never cross. They can be intersecting in one point. Or they can be the same line, have same points in everywhere.

Write a program to find intersection point of two different lines in 2D space. If they are parallel, return None.

We can use Python's [SymPy](https://www.sympy.org/) package. SymPy are capable of computing symbolic expressions with variables. And it has built-in Point and Line classes that we can use. You can learn more about sympy from [this tutorials](https://docs.sympy.org/1.5.1/tutorial).

There are two ways to represent a line, using a point on the line and the slope of line, or using two different points on the line. We will use two points.

### Practical - Line Intersection

- Using SymPy

```python
from sympy import Point, Line

line1 = Line(Point(-3, 0.5), Point(1, 1))
line2 = Line(Point(-2,-5), Point(3, 3))

intersect = line1.intersection(line2)
print(intersect)
```

- Classical Formula

<p align="center"><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c51a9b486a6ef5a7a08b92d75e71a07888034a9a" width=300></p>

```python
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

line1 = Line(Point(-3, 0.5), Point(1, 1))
line2 = Line(Point(-2,-5), Point(3, 3))

def findIntersection(l1, l2):
        x1, y1, x2, y2 = l1.p1.x, l1.p1.y, l1.p2.x, l1.p2.y
        x3, y3, x4, y4 = l2.p1.x, l2.p1.y, l2.p2.x, l2.p2.y
        
        px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        return px, py

x, y = findIntersection(line1, line2)
print(x, y)
```