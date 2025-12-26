import requests
from typing import List


class Brewery:
    def __init__(self, name: str, city: str, state: str, brewery_type: str):
        self.name = name
        self.city = city
        self.state = state
        self.brewery_type = brewery_type

    def __str__(self) -> str:
        return f"Browar: {self.name} ({self.city}, {self.state}) - Typ: {self.brewery_type}"


def pobierz_browary() -> List[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    response = requests.get(url)
    dane = response.json()

    lista_browarow = []

    for wpis in dane:
        nowy_browar = Brewery(
            str(wpis.get("name")),
            str(wpis.get("city")),
            str(wpis.get("state_province")),
            str(wpis.get("brewery_type"))
        )
        lista_browarow.append(nowy_browar)

    return lista_browarow


browary = pobierz_browary()

for b in browary:
    print(b)
