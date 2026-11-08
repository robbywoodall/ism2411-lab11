# --- Exercise 1 ---
customer = {
    "name": "Cooper",
    "email": "shoigoi@minecraft.net",
    "tier": "Gold",
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
