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
