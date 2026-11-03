file = open("orders.txt", "w")

file.write("Pizza\n")
file.write("Burger\n")
file.write("Pasta\n")
file.write("Sandwich\n")
file.write("Dosa\n")

file.close()

file = open("orders.txt", "r")

while True:
    order = file.readline()

    if not order:
        break

    print(order.strip())
    print("Position:", file.tell())

file.close()