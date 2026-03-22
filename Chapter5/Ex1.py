import matplotlib.pyplot as plt
labels = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]
plt.bar(labels, values)
plt.title("Kết quả học tập của lớp")
plt.xlabel("Mức học lực")
plt.ylabel("Số học sinh")
plt.show()
