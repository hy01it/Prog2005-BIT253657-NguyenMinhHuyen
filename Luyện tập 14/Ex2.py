names = []
for i in range(5):
    names.append(input(f"Nhập tên người thứ {i+1}: "))
print("Danh sách ban đầu:", names)
del names[1]
print("Danh sách sau khi xóa vị trí thứ 2:", names)
