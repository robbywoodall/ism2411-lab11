# --- Reflection 1 ---
# In the real world, customers may not always provide you with all of their data. There could be multiple instances
# in a customer's data where information is blank. If a key doesn't exist, use a reasonable default defined by the data being collected.
# --- Reflection 2 ---
# According to the reading, it is supposed to be similar to VLOOKUP from excel. The dictionary is the lookup table. 
# Python dictionaries can make looking up more efficient.
# --- Exercise 1 ---
customer = {
    "name": "Cooper",
    "email": "shoigoi@minecraft.net",
    "tier": "gold",
    "ytd_spend": "30500",
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
# --- Exercise 2 ---
customer["phone"] = "7278087470"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)
# --- Exercise 3 ---
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError caught! No email. Use .get for error checking!")
# --- Exercise 4 ---
for key in customer: #without .items() only looks at the labels on the folders
    print(key, customer[key])
for key, val in customer.items(): #with .items() gives the matched set on every pass
    print(f"{key}: {val}")
# --- Exercise 5 ---
purchase = 200
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount)
print(f"Tier: {customer['tier']}  Discount: {discount*100:.0f}%  Final: ${final_price:.2f}")
# --- Exercise 6 ---
purchase_six = 300
customers = [
    {
        "name": "Cooper",
        "tier": "platinum",
        "ytd_spend": "30500"
    },
    {
        "name": "Alex",
        "tier": "gold",
        "ytd_spend": "15000"
    },
    {
        "name": "Morgan",
        "tier": "silver",
        "ytd_spend": "5000"
    }
]
for c in customers:
    cust_discount = tier_discounts.get(c["tier"], 0)
    cust_final_price = purchase_six * (1 - cust_discount)
    
    print(f"Customer: {c['name']} | Tier: {c['tier']} | Discount: {cust_discount*100:.0f}% | Final Price: ${cust_final_price:.2f}")
# --- Exercise 7 ---
catalog = {"Widget A": {"price": 9.99, "stock": 150}, "Gadget C": {"price": 49.99, "stock": 8}}
for product_name, product_info in catalog.items():
    current_stock = product_info["stock"]
    if current_stock < 20:
        print(f"Low Stock Alert! {product_name} only has {current_stock} items left!")
# --- Exercise 8 ---
transactions = [
    {"region": "East", "amount": 200},
    {"region": "West", "amount": 150},
    {"region": "East", "amount": 300},
    {"region": "South", "amount": 100},
    {"region": "West", "amount": 250},
    {"region": "South", "amount": 400},
]
sales_summary = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_summary[region] = sales_summary.get(region, 0) + amount
for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]:.2f}")
print(sales_summary)