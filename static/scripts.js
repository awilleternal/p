document.addEventListener('DOMContentLoaded', () => {
    const addBookForm = document.getElementById('addBookForm');
    const availableBooksList = document.getElementById('availableBooks');
    const borrowIsbn = document.getElementById('borrowIsbn');
    const returnIsbn = document.getElementById('returnIsbn');

    // Fetch available books
    function fetchBooks() {
        fetch('/books')
            .then(response => response.json())
            .then(books => {
                availableBooksList.innerHTML = '';
                books.forEach(book => {
                    const li = document.createElement('li');
                    li.textContent = `${book.title} by ${book.author} (ISBN: ${book.isbn})`;
                    availableBooksList.appendChild(li);
                });
            });
    }

    // Add a book
    addBookForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const isbn = document.getElementById('isbn').value;
        const title = document.getElementById('title').value;
        const author = document.getElementById('author').value;
        const year = document.getElementById('year').value;

        fetch('/books', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ isbn, title, author, year })
        }).then(() => {
            fetchBooks();
        });
    });

    // Borrow a book
    document.getElementById('borrowBook').addEventListener('click', () => {
        const isbn = borrowIsbn.value;
        fetch(`/books/borrow/${isbn}`, { method: 'POST' })
            .then(() => fetchBooks());
    });

    // Return a book
    document.getElementById('returnBook').addEventListener('click', () => {
        const isbn = returnIsbn.value;
        fetch(`/books/return/${isbn}`, { method: 'POST' })
            .then(() => fetchBooks());
    });

    // Initial load
    fetchBooks();
});
