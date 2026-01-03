# Користувач вводить рядок і символ
text = input("Введіть рядок: ")
char = input("Введіть символ: ")

# Перевіряємо кількість входжень символу
if text.count(char) == 0:
    print(-2)
elif text.count(char) == 1:
    print(-1)
else:
    # Знаходимо індекс другої появи
    first_index = text.find(char)
    second_index = text.find(char, first_index + 1)
    print(second_index)