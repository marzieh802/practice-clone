class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def show_info(self):
        print(
            f"\nproduct : {self.name}\nprice : {self.price}\nquantity : {self.quantity}\ncategory : {self.category}")

    def update_price(self, new_price):
        if new_price <= 0:
            raise Exception("invalid price")
        else:
            self.price = new_price

    def add_stock(self, amount):
        if amount <= 0:
            raise Exception("invalid amount")
        else:
            self.quantity += amount

    def sell(self, amount):
        if self.quantity < amount:
            raise Exception("insufficent quantity")
        elif amount <= 0:
            raise Exception("invalid sell amount")
        else:
            self.quantity -= amount

    def __eq__(self, other):
        return self.name == other.name and self.category == other.category

    def __str__(self):
        return f"\nproduct : {self.name}\nprice : {self.price}\nquantity : {self.quantity}\ncategory : {self.category}"


product1 = Product("laptop", 1200, 5, "electronics")
product2 = Product("mouse", 25, 20, "accessories")
product3 = Product("laptop", 2, 8, "electronics")

# product1.show_info()
# product2.show_info()
# print(product1 == product2)
# print(product1 == product3)
# try:
#     product1.update_price(-100)
#     product1.show_info()
# except Exception as error:
#     print(f"error is: {error}")
# try:
#     product2.update_price(-10)
#     product2.show_info()
# except Exception as error:
#     print(f"error is: {error}")

print("\n\n")

try:
    product2.sell(30)
    product2.show_info()
except Exception as err:
    print(f"error is: {err}")
else:
    print("else foooor product2")
finally:
    product2.show_info()
try:
    product3.sell(5)
    product3.show_info()
except Exception as err:
    print(f"error is: {err}")
else:
    print("else foooor product3")

print(product1)
