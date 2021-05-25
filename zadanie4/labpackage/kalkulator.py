def kalkulator():
    liczba1 = input('Podaj piewszą liczbę')
    liczba2 = input('Podaj drugą liczbę')
    liczba1 = float(liczba1)
    liczba2 = float(liczba2)
    operacja = input('Podaj operację (+, -, *, /) >  ')
    try:
        if operacja == '+':
            wynik = liczba1 + liczba2
        elif operacja == '-':
            wynik = liczba1 - liczba2
        elif operacja == '*':
            wynik = liczba1 * liczba2
        elif operacja == '/':
            wynik = liczba1 / liczba2
        else:
            print('Błędna operacja')

        print(f'{liczba1} {operacja} {liczba2} = {wynik}')
    except ZeroDivisionError:
        print('Nie dziel przez zero')



