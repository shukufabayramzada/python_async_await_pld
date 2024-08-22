from typing import Dict

class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def remove_product(self, name: str, quantity: int) -> None:
        if name in self.products:
            if quantity >= self.products[name].quantity:
                del self.products[name]
            else:
                self.products[name].quantity -= quantity

    def get_inventory(self) -> Dict[str, Product]:
        return self.products

def main():
    inventory = Inventory()

    inventory.add_product(Product("Apple", 50))
    inventory.add_product(Product("Banana", 30))
    inventory.add_product(Product("Orange", 20))
    inventory.add_product(Product("Kiwi", 40))

    print("Initialization of the  Inventory:")
    for product in inventory.get_inventory().values():
        print(product)

    inventory.remove_product("Apple", 10)
    inventory.remove_product("Banana", 30)

    print("\nInventory after removal:")
    for product in inventory.get_inventory().values():
        print(product)

if __name__ == "__main__":
    main()
