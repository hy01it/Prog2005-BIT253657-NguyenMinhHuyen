students = {"Nam": 8,
            "Lan": 9,
            "Huy": 7}
def diem_trung_binh(data):
    tong = sum(data.values())
    return tong / len(data)
print("Điểm trung bình:", diem_trung_binh(students))
