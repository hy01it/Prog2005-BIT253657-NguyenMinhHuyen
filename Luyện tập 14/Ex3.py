n = int(input("Nhập số lượng phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Nhập phần tử {i+1}: ")))
odd_numbers = [x for x in arr if x % 2 != 0]
print("Các số lẻ:", odd_numbers, "| Tổng số lượng:", len(odd_numbers))
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
prime_numbers = [x for x in arr if is_prime(x)]
print("Các số nguyên tố:", prime_numbers)
