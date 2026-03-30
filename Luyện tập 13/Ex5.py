class Flower:
    def __init__(self, color):
        self._color = color   # thuộc tính private
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color
f = Flower("Đỏ")
print("Màu hoa:", f.get_color())
f.set_color("Vàng")
print("Màu hoa mới:", f.get_color())
