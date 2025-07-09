# Step 1: Original tuple (product, price, quantity)
product_info = ("Laptop", 1200.00, 2)

# Step 2: Unpack the tuple into separate variables
product, price, quantity = product_info

# Step 3: Calculate total cost
total_cost = price * quantity
print(f"Product: {product}")
print(f"Price per unit: ${price}")
print(f"Quantity: {quantity}")
print(f"Total cost: ${total_cost}")

# Step 4: Convert tuple to list to modify quantity
product_list = list(product_info)
product_list[2] = 3  # New quantity

# Step 5: Convert back to tuple
updated_product_info = tuple(product_list)

# Step 6: Print updated values
print("\nUpdated product info:")
product, price, quantity = updated_product_info
total_cost = price * quantity
print(f"Product: {product}")
print(f"Price per unit: ${price}")
print(f"Quantity: {quantity}")
print(f"Total cost: ${total_cost}")
