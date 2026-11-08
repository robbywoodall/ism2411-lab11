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