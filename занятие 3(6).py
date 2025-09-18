def f(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        return 'Да'
    else:
        return 'Нет'
print(f(8, 8, 8, 8))