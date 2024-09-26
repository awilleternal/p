    def test_borrow_book(self):
        book_data = {
            'isbn': '978-3-16-148410-0',
            'title': 'Test Book',
            'author': 'Author',
            'year': 2023
        }
        self.app.post('/books', data=json.dumps(book_data), content_type='application/json')
        
        response = self.app.post(f'/books/borrow/{book_data["isbn"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book borrowed successfully', response.data)

    def test_borrow_unavailable_book(self):
        response = self.app.post('/books/borrow/1234567890')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Book not available or already borrowed', response.data)
