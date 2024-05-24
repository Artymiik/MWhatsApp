def FORMAT_PHONE(phones):
  final_phones = []

  for phone in phones:
    if not phone.startswith("+") and not phone.startswith("wa.me/"):
      phone = "+" + phone
    elif phone.startswith("wa.me/"):
      phone = phone.replace("wa.me/", "+")

    final_phones.append(phone)

  return final_phones