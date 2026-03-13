s = input("Nhập chuỗi số (vd: 5;7;8;-2;8;11;13;9;10): ")
nums = list(map(int, s.split(";")))
print("Các số:")
for num in nums:
    print(num)
even = sum(1 for x in nums if x % 2 == 0)
negative = sum(1 for x in nums if x < 0)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
prime_count = sum(1 for x in nums if is_prime(x))
avg = sum(nums) / len(nums)
print("Số chẵn:", even)
print("Số âm:", negative)
print("Số nguyên tố:", prime_count)
print("Trung bình:", avg)
