n = int(input())
if n >= 1440:
    c = n // 1440
    n -= 1440 * c
    min = n % 60
    chas = n // 60
    if min < 10:
        min = '0' + str(min)
else:
    min = n % 60
    chas = n // 60
    if min < 10:
        min = '0' + str(min)
print(chas, ':', min, sep='')

