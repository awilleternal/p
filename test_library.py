import unittest
import json
from library import app, library

class LibraryManagementTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        library.books = []  # Reset books

    def test_add_book(self):
        book_data = {
            'isbn': '978-3-16-148410-0',
            'title': 'Test Book',
            'author': 'Author',
            'year': 2023
        }
        response = self.app.post('/books', data=json.dumps(book_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Book added successfully', response.data)

if __name__ == '__main__':
    unittest.main()
