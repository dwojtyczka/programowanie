import magazine.utils

class Product:
    def __init__(self, name):
        self.name = name
        magazine.utils.log_info(f"Utworzono produkt: {name}")
