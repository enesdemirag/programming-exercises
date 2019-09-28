### Theoretical - Line Intersection

We will use vectors and constants. Solve k1v1 == k2v2

### Practical - Line Intersection

```python
class Line(object):
    """
    y - y1 = m * (x - x1)
    point = (x1, y1)
    slope = m
    """
    def __init__(self, point, slope):
        self.x = point[0]
        self.y = point[1]
        self.slope = slope

def intersection(l1, l2):
    intersection_point = (0, 0)
    return intersection_point

line1 = Line((3, 3), 0.5)
line2 = Line((-2,-5), -1)
point = intersection(line1, line2) # (-6, -1)
print(point)
```