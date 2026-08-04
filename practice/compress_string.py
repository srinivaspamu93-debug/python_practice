alphabet = input("Enter a string: ")
compress = {}
sequence = []
for char in alphabet:
    if char in compress:
        compress[char] = compress[char] + 1
    else:
        compress[char] = 1
        sequence.append(char)
print(compress)
final_string = ""
for j in sequence:
    final_string = final_string + j + str(compress[j])

print(final_string)