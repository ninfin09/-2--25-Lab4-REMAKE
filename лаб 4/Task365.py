s = input("Введіть рядок: ")
result = ""
i = 0

while i < len(s):
    char = s[i]
    if i > 0 and 'A' <= char <= 'Z':
        result = result + " " + char
    else:
        result = result + char
    i = i + 1

print(result)