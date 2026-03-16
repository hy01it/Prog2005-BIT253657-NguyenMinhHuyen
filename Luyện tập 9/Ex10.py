class SinhVien:
    def __init__(self, diem):
        self.diem = diem
    def __eq__(self, other):
        return self.diem == other.diem
sv1 = SinhVien(8)
sv2 = SinhVien(8)
sv3 = SinhVien(9)
print("sv1 == sv2:", sv1 == sv2)
print("sv1 == sv3:", sv1 == sv3)
