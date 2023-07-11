from book import Book

def test_book_initialization():
    someBook = Book("fe23f3", "Once upon a time..")
    assert someBook.id == "fe23f3"
    assert someBook.content == "Once upon a time.."