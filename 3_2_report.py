print(f"{'Product':<15} {'Price':<12} {'Quantity':<15} {'Total':<12}")
print("-" * 60)

products = [("Chicken", 5.99, 10), ("Beef", 7.99, 8), ("Fish", 6.49, 12), ("Pork Chops", 3.99, 15), ("Lobster", 4.49, 20)]

for name, price, quantity in products:
    total = price * quantity
    print(f"{name:<15} ${price:<11.2f} {quantity:<15} ${total:<11.2f}")

print("-" * 60)

grand = sum(price * quantity for _, price, quantity in products)
print(f"{'Grand Total':<15} {'':>20}   ${grand:<11.2f}")