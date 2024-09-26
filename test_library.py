class LibraryManagementTestCase(unittest.TestCase):
    
    def test_add_book(self):
        # Define book data
        book_data = {
            'isbn': '978-3-16-148410-0',
            'title': 'Test Book',
            'author': 'Author',
            'year': 2023
        }
        
        # Make POST request to add a book
        response = self.app.post('/books', data=json.dumps(book_data), content_type='application/json')
        
        # Verify if the book was added successfully
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Book added successfully', response.data)

if __name__ == '__main__':
    unittest.main()
