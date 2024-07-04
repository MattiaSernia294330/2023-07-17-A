from dataclasses import dataclass
@dataclass
class Product():
    Product_number:int
    Product:str
    def __hash__(self):
        return hash(self.Product_number)