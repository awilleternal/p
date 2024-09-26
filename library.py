class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book not in self.borrowed_books:
                self.borrowed_books.append(book)
                return
        raise ValueError("Book not available or already borrowed")

@app.route('/books/borrow/<isbn>', methods=['POST'])
def borrow_book(isbn):
    try:
        library.borrow_book(isbn)
        return jsonify({'message': 'Book borrowed successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
