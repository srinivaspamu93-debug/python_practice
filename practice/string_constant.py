keepconstant = "G20R1K4A9N46X7D8C0B3M5Z6"

numbers = []

for char in keepconstant:
    if char.isdigit():
        numbers.append(char)

numbers.reverse()

result = ""
index = 0

for char in keepconstant:
    if char.isdigit():
        result += numbers[index]
        index += 1
    else:
        result += char

print(result)