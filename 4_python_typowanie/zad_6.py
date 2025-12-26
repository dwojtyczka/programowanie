def przetworz_listy(lista1: list, lista2: list) -> list:
    polaczona = lista1 + lista2
    bez_duplikatow = list(set(polaczona))
    wynik = [x ** 3 for x in bez_duplikatow]
    return wynik

l1 = [1, 2, 2]
l2 = [2, 3, 4]

print(przetworz_listy(l1, l2))
