n = 5  # maksymalna liczba gwiazdek w wierszu
i = 1  # licznik wierszy
while i < 2 * n:
    if i <= n:
        print('* ' * i)          # część rosnąca
    else:
        print('* ' * (2 * n - i))  # część malejąca
    i += 1