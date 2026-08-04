
prime_number = []
for j in range(1,52):
    number = j
    times = 0
    for i in range(2,number):
        if number % i != 0:
            times = times + 1

    if times == number - 2:
        print("prime", number)
        prime_number.append(number)
    else:
        print("not prime",number)
print(prime_number)