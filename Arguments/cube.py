def cube1(num1):
    c1=num1**3
    return c1
def cube2(c1):
    return cube1(c1**3)

print(cube2(5))