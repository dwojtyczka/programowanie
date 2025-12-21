def wypisz_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

moje_liczby = list(range(10))

wypisz_parzyste(moje_liczby)
