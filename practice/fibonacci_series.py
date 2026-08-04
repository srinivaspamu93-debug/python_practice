number = int(input("Enter a number: "))

a, b = 4,7

for i in range(number):
    print(a, end =" ")
    c = a + b
    a = b
    b = c
