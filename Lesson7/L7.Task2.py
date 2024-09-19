# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.

def compute_total_stock_value(stock, prices):
    total_value = 0
    for item in stock:
        if item in prices:
            total_value += stock[item] * prices[item]
    return total_value


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_stock_value = compute_total_stock_value(stock, prices)
print(f"Total stock value is: {total_stock_value}")
