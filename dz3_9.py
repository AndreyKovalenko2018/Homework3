#9
def distance(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    return (a*a + b*b)**0.5
print(distance(1,1,0,0))

