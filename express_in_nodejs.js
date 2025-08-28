const express = require('express');
const app = express();
const port = 8000;

// Middleware to parse JSON request bodies
app.use(express.json());

// Dummy data
let books = [
  { id: 1, book: "Never Lie" },
  { id: 2, book: "Mrityunjay" }
];

// GET - fetch all books
app.get('/books', (req, res) => {
  res.json(books);
});

// POST - add a new book
app.post('/books', (req, res) => {
  const newBook = {
    id: books.length + 1,
    book: req.body.book   
  };
  books.push(newBook);
  res.status(201).json(newBook);
});

// PUT - update a book by id
app.put('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const book = books.find(b => b.id === id);

  if (!book) {
    return res.status(404).json({ message: "Book not found" });
  }

  book.book = req.body.book || book.book;  
  res.json(book);
});

// DELETE - remove a book by id
app.delete('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  books = books.filter(b => b.id !== id);
  res.json({ message: `Book with id ${id} deleted` });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
