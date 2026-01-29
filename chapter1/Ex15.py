for i in range(1, 4):
    name = input("Nhập tên sinh viên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))

    avg = (toan + ly + hoa) / 3
    print(f"Sinh viên {name} có điểm trung bình: {avg:.2f}")
