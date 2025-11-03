#Write a program which gets a phone number from a form input or terminal.
#  Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1..

phone = input("Enter phone number: ").strip()

if phone.startswith("+254"):
    phone = phone
elif phone.startswith("254"):
    phone = "+" + phone
elif phone.startswith("0"):
    phone = "+254" + phone[1:]
elif phone.startswith("7") or phone.startswith("1"):
    phone = "+254" + phone
else:
    phone = " Invalid phone number format."

print("Converted Number:", phone)
