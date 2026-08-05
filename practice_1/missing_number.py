array = [1,2,4,6,8,14,11,17,19]
number = 20

for num in range(1,number+1):
    if num in array:
        continue

    print(num,end=" ")