def f(x, y, z):
    cnt = x + y + z
    if x == y == z:
        return '3'
    if x == y != z or x == z != y or z == y != x:
        return '2'
    else:
        return '0'
print(f(4, 3, 3))