books = [
    ("Book 1", 30000),
    ("Book 2", 50000),
    ("Book 3", 100000)
]
total = 0
with open("books.txt", "w", encoding="utf-8") as f:
    for name, price in books:
        f.write(f"{name};{price}\n")
        total += price
    f.write(f"Tong;{total}")
