# Discount Calculator Program

print("--- Discount Calculator ---")

# User se input lena
original_price = float(input("Item ki Original Price (₹) enter karein: "))
discount_percentage = float(input("Discount Percentage (%) enter karein: "))

# Discount amount nikalna
discount_amount = (original_price * discount_percentage) / 100

# Final price nikalna
final_price = original_price - discount_amount

# Results print karna
print("\n--- Bill Details ---")
print(f"Original Price    : ₹{original_price:.2f}")
print(f"Discount Included : ₹{discount_amount:.2f} ({discount_percentage}%)")
print(f"Final Payable Price: ₹{final_price:.2f}")