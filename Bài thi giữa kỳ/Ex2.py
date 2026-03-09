or i in range(111, 16, -1):
    if i % 2 != 0:
        print(i, end=" ")
for num in range(17, 112):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
