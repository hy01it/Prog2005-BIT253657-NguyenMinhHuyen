s = input("Nhập chuỗi: ")
upper = lower = digit = special = space = vowel = consonant = 0
vowels = "aeiouAEIOU"
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    if ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    elif not ch.isalnum():
        special += 1
    if ch in vowels:
        vowel += 1
    elif ch.isalpha():
        consonant += 1
print("Chữ hoa:", upper)
print("Chữ thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
print("Khoảng trắng:", space)
print("Nguyên âm:", vowel)
print("Phụ âm:", consonant)
