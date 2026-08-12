text = "1F9M7N4V2A8Z6J4D8"

# Extract letters and reverse them
letters = [char for char in text if char.isalpha()]
letters.reverse()

# Replace letters while keeping numbers in their positions
result = []
letter_index = 0

for char in text:
    if char.isalpha():
        result.append(letters[letter_index])
        letter_index += 1
    else:
        result.append(char)

result = "".join(result)

print(result)

