def f(n):
    if n % 4 != 0 or n % 100 == 0 and n % 400 != 0:
        return 'Нет'
    else:
        return 'Да'
print(f(344))

