ukr_upp_char = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
ukr_low_char = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

text = input("write message: ")
a = input("c cifer d decifer q quit:")
k = 3
n = len(ukr_low_char)

if a == "c":
    encrypted = ""
    for ch in text:
        if ch in ukr_upp_char:
            i = ukr_upp_char.index(ch)
            encrypted += ukr_upp_char[(i + k) % n]
        elif ch in ukr_low_char:
            i = ukr_low_char.index(ch)
            encrypted += ukr_low_char[(i + k) % n]
        else:
            encrypted += ch
    print("Зашифровано:", encrypted)

elif a == "d":
    decrypted = ""
    for ch in text:
        if ch in ukr_upp_char:
            i = ukr_upp_char.index(ch)
            decrypted += ukr_upp_char[(i - k) % n]
        elif ch in ukr_low_char:
            i = ukr_low_char.index(ch)
            decrypted += ukr_low_char[(i - k) % n]
        else:
            decrypted += ch
    print("Розшифровано:", decrypted)
elif a == "q":
    print("thank you for a game")





