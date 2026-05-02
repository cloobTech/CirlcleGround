




def normalize_phone_numbers(phone_number: str):
    phone_number = phone_number.replace(" ", "")
    if phone_number.startswith("+234"):
        phone_number = phone_number[4:]
    elif phone_number.startswith("234"):
        phone_number = phone_number[3:]
    elif phone_number.startswith("0"):
        phone_number = phone_number[1:]
    return phone_number