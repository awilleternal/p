from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

class Book:
    def __init__(self, isbn, title, author, year):
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

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

    def return_book(self, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                self.borrowed_books.remove(book)
                return
        raise ValueError("Book was not borrowed")

    def get_available_books(self):
        return [book for book in self.books if book not in self.borrowed_books]

library = Library()

# Serve the index.html file from the templates directory
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books():
    available_books = library.get_available_books()
    return jsonify([{
        'isbn': book.isbn,
        'title': book.title,
        'author': book.author,
        'year': book.year
    } for book in available_books])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book = Book(data['isbn'], data['title'], data['author'], data['year'])
    library.add_book(book)
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books/borrow/<isbn>', methods=['POST'])
def borrow_book(isbn):
    try:
        library.borrow_book(isbn)
        return jsonify({'message': 'Book borrowed successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/books/return/<isbn>', methods=['POST'])
def return_book(isbn):
    try:
        library.return_book(isbn)
        return jsonify({'message': 'Book returned successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
