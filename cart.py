class Cart():

    def __init__(self):
        self.cart = []

    def add_item(self, product, quantity):
        self.cart.append( (product, quantity) )

    def sum(self):
        sum = 0
        for product, quantity in self.cart:
            sum += product.total_price(quantity)
        return sum

if __name__ == '__main__':
    from products import PhysicalProduct, DigitalProduct, SubscriptionProduct
    product = PhysicalProduct(name = "teacup", price = 10, weight = 300)
    cart = Cart()
    cart.add_item(product = product, quantity= 5)
    cart.add_item(product = DigitalProduct(name = "ebook", price = 50, link = "https://amazon.com"), quantity= 1)
    cart.add_item(product = SubscriptionProduct(name = "ebook", price = 50, link = "https://genius.com"), quantity= 1)
    print("Total sum of cart -> ", cart.sum())
