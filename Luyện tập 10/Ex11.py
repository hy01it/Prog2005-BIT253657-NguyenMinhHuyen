import math
def bai1():
    def get_filename(path):
        return path.split("\\")[-1]
    def get_name(path):
        filename = get_filename(path)
        return filename.split(".")[0]
    path = "d:\\music\\muabui.mp3"
    print("Tên file:", get_filename(path))
    print("Tên bài:", get_name(path))

def bai2():
    s = input("Nhập chuỗi: ")
    ch = input("Nhập ký tự: ")
    count = s.count(ch)
    print("Số lần xuất hiện:", count)

def bai3():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    n = int(input("Nhập n: "))
    print("Giai thừa:", factorial(n))

def bai4():
    s = input("Nhập chuỗi: ")
    if s == "":
        print("Lỗi: chuỗi rỗng")
    else:
        print("Độ dài:", len(s))

def bai5():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(x, x ** 2)
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.subplot(1, 2, 2)
    plt.plot(x, np.sqrt(x))
    plt.title("y = sqrt(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def bai6():
    s = input("Nhập chuỗi: ")
    rev = ""
    for ch in s:
        rev = ch + rev
    print("Chuỗi đảo:", rev)

def bai7():
    while True:
        pw = input("Nhập mật khẩu: ")
        if pw == "python123":
            print("Đúng mật khẩu")
            break
        else:
            print("Sai, nhập lại")

def bai8():
    arr = []
    for i in range(5):
        arr.append(input(f"Nhập chuỗi {i + 1}: "))
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Bước {i + 1}:", arr)

def bai9():
    class Person:
        count = 0
        def __init__(self, name, age):
            if age < 0:
                raise ValueError("Tuổi không hợp lệ")  # cách 1
            self._name = name
            self._age = age
            Person.count += 1
        @property
        def age(self):
            return self._age
        @age.setter
        def age(self, value):
            if value < 0:
                raise ValueError("Tuổi phải >= 0")  # cách 2
            self._age = value
        def __str__(self):
            return f"{self._name} - {self._age}"
        def say_hello(self):
            print("Xin chào!")
        @classmethod
        def get_count(cls):
            return cls.count
        @staticmethod
        def is_adult(age):
            return age >= 18
        def __eq__(self, other):
            return self._age == other._age
    class Student(Person):
        def __init__(self, name, age, score):
            super().__init__(name, age)
            self.score = score
        def study(self):
            print("Đang học...")
    s1 = Student("An", 20, 8)
    s2 = Student("Bình", 20, 9)
    print(s1)
    s1.say_hello()
    s1.study()
    print("Số đối tượng:", Person.get_count())
    print("So sánh:", s1 == s2)
    print("Trưởng thành:", Person.is_adult(20))

def bai10():
    arr = []
    for i in range(5):
        arr.append(input(f"Nhập chuỗi {i + 1}: "))
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Bước {i + 1}:", arr)

while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("5. Bài 5")
    print("6. Bài 6")
    print("7. Bài 7")
    print("8. Bài 8")
    print("9. Bài 9")
    print("10. Bài 10")
    print("0. Thoát")
    choice = input("Chọn: ")
    if choice == "1":
        bai1()
    elif choice == "2":
        bai2()
    elif choice == "3":
        bai3()
    elif choice == "4":
        bai4()
    elif choice == "5":
        bai5()
    elif choice == "6":
        bai6()
    elif choice == "7":
        bai7()
    elif choice == "8":
        bai8()
    elif choice == "9":
        bai9()
    elif choice == "10":
        bai10()
    elif choice == "0":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")
