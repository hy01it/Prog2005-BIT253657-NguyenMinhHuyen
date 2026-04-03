from Script34 import Book
books = [
    Book("Book 1", 30000),
    Book("Book 2", 50000),
    Book("Book 3", 100000)
]

tong_tien = sum(book.price for book in books)

file_path = "books.txt"

try:
    with open(file_path, "w", encoding="utf-8") as f:
        # Ghi thông tin từng cuốn sách
        for book in books:
            f.write(f"{book.name};{book.price}\n")

        f.write(f"Tong;{tong_tien}")

    print(f"Đã lưu thông tin vào file '{file_path}' thành công!")

except Exception as e:
    print(f"Có lỗi xảy ra khi ghi file: {e}")
