# Wersja 1: Pętla for
def pomnoz_przez_dwa_petla(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


# Wersja 2: Lista składana
def pomnoz_przez_dwa_skladana(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


# Test
liczby = [1, 2, 3, 4, 5]

print("Pętla for:", pomnoz_przez_dwa_petla(liczby))
print("Lista składana:", pomnoz_przez_dwa_skladana(liczby))
