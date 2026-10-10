import re

text = "Customer review: Food was good. Contact: 9876543210 for details."

match = re.search(r"\b[0-9]{10}\b", text)

if match:
    print("Mobile number:", match.group())
else:
    print("Mobile number not found")