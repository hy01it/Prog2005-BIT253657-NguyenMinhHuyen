class SinhVien:
    count = 0
    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1
    @classmethod
    def dem_so_sv(cls):
        return cls.count
sv1 = SinhVien(7)
sv2 = SinhVien(8)
sv3 = SinhVien(9)
print("Số sinh viên đã tạo:", SinhVien.dem_so_sv())
