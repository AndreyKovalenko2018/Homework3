#7
def triangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        if a==b==c:
          return 'Equilateral triangle'
        elif ((a==b and a!=c and b!=c) or (a==c and a!=b and b!=c) or (b==c and a!=b and a!=c)):
            return 'Isosceles triangle'
        elif (a!=b and a!=c and b!=c):
            return 'Versatile triangle'
    else:
        return 'Not a triangle'

print(triangle(7,1,7))