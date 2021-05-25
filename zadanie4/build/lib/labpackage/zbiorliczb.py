def zbior_liczb():
    for liczba in [3, 6, 8, 2, 1, 76, -2, -7, -76, 0]:
        if liczba > 0:
            print(f'{liczba} jest większa od 0.')
        elif liczba < 0:
            print(f' {liczba} jest mniejsza od 0.')
        else:
            print('Liczba jest zerem!')
