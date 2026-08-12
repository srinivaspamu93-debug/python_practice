text = "1F9M7N4V2A8Z6J4D8"

chars = list(text)

left = 0
right = len(chars) - 1

while left < right:

    # Find next alphanumeric characters
    if not chars[left].isalnum():
        left += 1
        continue

    if not chars[right].isalnum():
        right -= 1
        continue

    chars[left], chars[right] = chars[right], chars[left]

    left += 1
    right -= 1

print("".join(chars))