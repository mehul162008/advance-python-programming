class InvalidCouponCodeError(Exception):
    pass


valid_codes = ["ZOMATO50", "FOOD20", "SAVE100"]

coupon = input("Enter coupon code: ")

try:
    if coupon not in valid_codes:
        raise InvalidCouponCodeError("Invalid coupon code")
    else:
        print("Coupon applied successfully")

except InvalidCouponCodeError as e:
    print(e)