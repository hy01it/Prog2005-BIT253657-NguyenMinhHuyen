class Student:
    def __init__(self, name, score):
        self.name = name
        if 0 <= score <= 10:
            self.score = score
        else:
            print("Điểm không hợp lệ")
            self.score = 0
