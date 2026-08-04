number = int(input("Enter a number: "))
factorial = 1

for fact in range(1, number+1):
    factorial *= fact

print(factorial)

print("-" * 13)

# recursion method

def factorial(number, result=1):
    if number == 0:
        return result
    return factorial(number - 1, result * number)

print(factorial(number))