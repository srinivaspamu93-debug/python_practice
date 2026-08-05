# for text or string

text = input("Enter a string: ")

reverse = ""

for char in range(len(text) - 1, -1, -1):
    reverse = reverse + text[char]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# for number or integer

number = int(input("Enter a number: "))

original = number
reverse = 0

length = len(str(number))

for num in range(length):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print(f"{original} is a Palindrome.")
else:
    print(f"{original} is Not a Palindrome.")