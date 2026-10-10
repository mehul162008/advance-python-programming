class PaymentFailedError(Exception):
    pass


def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Payment failed: Invalid amount")

    print("Payment Successful")


try:
    amount = float(input("Enter payment amount: "))
    process_payment(amount)

except PaymentFailedError as e:
    print(e)