from products import PhysicalProduct, DigitalProduct

teacup = PhysicalProduct(name = "Teacup", price= 20, weight= 300)
ebook = DigitalProduct(name = "Python for dummies", price = 30, link = "https://amazon.com/python-for-dummies.html")

campaign = [teacup]

def apply_discount(products, d):
    for product in products:
        # product.price = product.price - d
        product.set_price(product.get_price() - d)

apply_discount(products=campaign, d = 10)

for product in campaign:
    print("Price after discount for ", product.name , " -> ", product.get_price())