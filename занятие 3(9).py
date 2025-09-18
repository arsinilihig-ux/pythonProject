def f(n, m, k):
    if (k % n == 0 or k % m == 0) and k != n * m:
        return 'Да'
    else:
        return 'Нет'
print(f(5, 5, 5))