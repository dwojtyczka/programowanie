def czy_zawiera(lista: list, wartosc: int) -> bool:
    return wartosc in lista


lista_liczb = [10, 20, 30, 40]
wynik = czy_zawiera(lista_liczb, 30)
print(wynik)
