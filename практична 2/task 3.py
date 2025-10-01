ukr_upp_char = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
ukr_low_char = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def caesar_cipher(text, k):
    result = ""
    n = len(ukr_low_char)
    for ch in text:
        if ch in ukr_upp_char:
            i = ukr_upp_char.index(ch)
            result += ukr_upp_char[(i + k) % n]
        elif ch in ukr_low_char:
            i = ukr_low_char.index(ch)
            result += ukr_low_char[(i + k) % n]
        else:
            result += ch  # якщо не літера — залишаємо як є
    return result

def caesar_decipher(text, k):
    return caesar_cipher(text, -k)

# приклад
msg = "Привіт Світ"
k = 3
enc = caesar_cipher(msg, k)
dec = caesar_decipher(enc, k)

print("Оригінал:", msg)
print("Зашифровано:", enc)
print("Розшифровано:", dec)
