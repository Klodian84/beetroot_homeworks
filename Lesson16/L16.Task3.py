class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0.0

    def add(self, product, amount):
        if product.name in self.products:
            self.products[product.name]["quantity"] += amount
        else:
            # Increase the price by 30%
            product_with_markup = {
                "product": product,
                "price": product.price * 1.3,
                "quantity": amount,
                "discount": 0
            }
            self.products[product.name] = product_with_markup

    def set_discount(self, identifier, percent, identifier_type="name"):

        for product_info in self.products.values():
            if identifier_type == "name" and product_info["product"].name == identifier:
                product_info["discount"] = percent
            elif identifier_type == "type" and product_info["product"].type == identifier:
                product_info["discount"] = percent

    def sell_product(self, product_name, amount):

        if product_name not in self.products:
            raise ValueError(f"Product {product_name} is not available in the store.")

        product_info = self.products[product_name]
        if product_info["quantity"] < amount:
            raise ValueError(f"Not enough {product_name} in stock.")

        final_price = product_info["price"] * (1 - product_info["discount"] / 100)

        self.income += final_price * amount

        product_info["quantity"] -= amount

    def get_income(self):

        return self.income

    def get_all_products(self):

        return [(product_info["product"].name, product_info["quantity"]) for product_info in self.products.values()]

    def get_product_info(self, product_name):

        if product_name in self.products:
            return product_name, self.products[product_name]["quantity"]
        else:
            raise ValueError(f"Product {product_name} is not available.")


# Example:

# Creating products
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

# Creating store
s = ProductStore()

# Adding products to the store
s.add(p, 10)
s.add(p2, 300)

# Selling products
s.sell_product('Ramen', 10)

# Getting product info
assert s.get_product_info('Ramen') == ('Ramen', 290)

# Setting discount for a product by name
s.set_discount('Ramen', 10)

# Getting the store's income
print(s.get_income())

# Listing all products in the store
print(s.get_all_products())
