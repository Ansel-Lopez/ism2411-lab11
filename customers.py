print("--- exercise 1 ---")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

print("--- exercise 2 ---")

customer["phone"] = "555-5555"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer['email']
print(customer)

print(customer.get('ytd_spend', 0))

print("--- exercise 3 ---")

print(customer.get('email', 'no email on file'))

try:
    print(customer['email'])
except KeyError as error:
    print("KeyError caught: ", error)

print('--- exercise 4 ---')

# Without .items(), the loop only returns the keys.
# We use each key to access its value from the dictionary.

for key, value in customer.items():
    print(f'{key}: {value}')

for something in customer:
    print(something, customer[something])

print('--- exercise 5 ---')
tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f'Tier: {customer["tier"]}')
print(f'Discount Rate: {discount_rate * 100}%')
print(f'Final Price: ${final_price:.2f}')

print('--- exercise 6 ---')

customers =  [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f'{record["name"]} ({record["tier"]}): ${discount:.2f} off a $300 purchase')

print('--- exercise 7 ---')

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")

print('--- exercise 8 ---')

sales_by_region = {}
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "North", "amount": 200}, 
]

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")

