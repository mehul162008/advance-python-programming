try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("Total price:", total)

except ValueError:
    print("Error: Please enter numeric values only.")