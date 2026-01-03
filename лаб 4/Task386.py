s = input("Введіть бінарну послідовність: ")

result = ""
zero_count = 0
i = 0

while i < len(s):
    char = s[i]
    
    if char == '0':
        # Якщо бачимо 0, просто рахуємо його
        zero_count = zero_count + 1
    elif char == '1':
        # Якщо бачимо 1, формуємо літеру
        # 'a' відповідає 0 нулів, тому додаємо zero_count до коду 'a'
        letter = chr(ord('a') + zero_count)
        result = result + letter
        # Скидаємо лічильник нулів для наступної літери
        zero_count = 0
    
    i = i + 1

print(result)