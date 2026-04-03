class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self): return self._name

    @name.setter
    def name(self, value): self._name = value

    @property
    def price(self): return self._price

    @price.setter
    def price(self, value): self._price = value

my_book = Book("Lập trình Python", 50000)
print(f"Giá của cuốn sách: {my_book.price}")
