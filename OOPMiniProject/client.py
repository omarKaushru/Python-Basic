from mobile_tech import Mobile
from laptop_tech import Laptop
from tech_product import Tech
from sales_person import SalesPerson
from datetime import date


phone_1 = Mobile('iphone_11', 60000, 500, 'Black', '1920-1080', 10)
phone_2 = Mobile('iphone_12', 70000, 550, 'Silver', '1920-1080', 12)
phone_3 = Mobile('iphone_13', 80000, 580, 'Project Red', '1920-1080', 13)

laptop_1 = Laptop('Asus g14', 130000, 1.6, 'Moonlight Silver', 16, 'Ryzen 4800H', 1000)
laptop_2 = Laptop('Macbook Pro 13', 130000, 1.7, 'Dark Grey', 8, 'Intel Core i5', 256)
laptop_3 = Laptop('Dell XPS 13', 140000, 1.4, 'White', 16, 'Intel Core i7', 512)


# Test Methods

print(laptop_1)
print(phone_1)

# Applying the discount upon the product
phone_1.apply_discount()
print(phone_1.price)

# Total number of products
print(Tech.get_total_products())

# Shipping Cost
print(laptop_3.calculate_shipping_cost(10))

# Setting the double price for the 1st laptop
print(laptop_1.price)
laptop_1.set_double_price()
print(laptop_1.price)

# Changing Specs for laptop 3
print(laptop_3)
laptop_3.change_specs(32, 1000)
print(laptop_3)

sales_person_1 = SalesPerson(
    'Majed',
    'Ali',
    40000,
    date(2020, 1, 5)
)

# Adding the products
sales_person_1.sell_product(phone_1)
sales_person_1.sell_product(phone_2)
sales_person_1.sell_product(laptop_1)
sales_person_1.sell_product(laptop_2)

# total products sold
print(sales_person_1.total_products_sold())

# Products sold:
sales_person_1.display_sales()

# Calculate Commission
print(sales_person_1.calculate_commission(0.2))

# Sort the sold products by price
sales_person_1.sort_by_price()
sales_person_1.display_sales()

