import re

def is_valid_pnr(pnr):
    return bool(re.match(r"^[0-9]{10}$", pnr))


pnr = input("Enter 10-digit PNR number: ")

if is_valid_pnr(pnr):
    print("Valid PNR format")
else:
    print("Invalid PNR format")