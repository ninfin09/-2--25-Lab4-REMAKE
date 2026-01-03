s = input("Введіть рядок: ")

def get_digits(text):
    if not text:
        return ""
    
    char = text[0]
    rest = text[1:]
    
    # Перевіряємо, чи є символ цифрою
    if '0' <= char <= '9':
        return char + get_digits(rest)
    else:
        return get_digits(rest)

print(get_digits(s))