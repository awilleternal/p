from flask import Flask, jsonify, request

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

    def add_book(self, book):
        self.books.append(book)

    def get_available_books(self):
        return self.books

library = Library()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book = Book(data['isbn'], data['title'], data['author'], data['year'])
    library.add_book(book)
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books', methods=['GET'])
def get_books():
    available_books = library.get_available_books()
    return jsonify([{
        'isbn': book.isbn,
        'title': book.title,
        'author': book.author,
        'year': book.year
    } for book in available_books])

if __name__ == '__main__':
    app.run(debug=True)
