try:
    a = int(input("Nhập số: "))
    b = int(input("Nhập số: "))
    print("Kết quả:", a / b)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
except ValueError:
    print("Lỗi: Phải nhập số nguyên")
