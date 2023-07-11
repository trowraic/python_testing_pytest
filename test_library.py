from library import Library
from book import Book
import pytest
from unittest.mock import Mock

@pytest.fixture()
def someEmptyLibrary():
    someLibrary = Library()
    return someLibrary

@pytest.fixture(scope="module")
def someLargeLibrary():
    someLibrary = Library()
    someLibrary.storeBook(Book("tgdi5", "The Great Debate, Issue 5"))
    someLibrary.storeBook(Book("tgdi1", "The Great Debate, Issue 1"))
    someLibrary.storeBook(Book("tgdi2", "The Great Debate, Issue 2"))
    someLibrary.storeBook(Book("tgdi4", "The Great Debate, Issue 4"))
    someLibrary.storeBook(Book("tgdi6", "The Great Debate, Issue 6"))
    someLibrary.storeBook(Book("tgdi3", "The Great Debate, Issue 3"))
    return someLibrary

def test_library_add_book(someEmptyLibrary, someLargeLibrary):
    someEmptyLibrary.storeBook(Book("asdfe", "Let me repeat myself, .."))
    assert someEmptyLibrary.countBooks() == 1
    someLargeLibrary.storeBook(Book("asdfe", "Let me repeat myself, .."))
    assert someLargeLibrary.countBooks() == 7

    with pytest.raises(ValueError):
        someEmptyLibrary.storeBook(Book("", "Let me repeat myself, .."))


def test_library_add_somethingElse(someEmptyLibrary):
    with pytest.raises(TypeError):
        someEmptyLibrary.storeBook("Test")
    assert someEmptyLibrary.countBooks() == 0

def test_library_add_duplicate(someEmptyLibrary):
    someEmptyLibrary.storeBook(Book("asdfe", "Let me repeat myself, .."))
    someEmptyLibrary.storeBook(Book("asdfe", "Let me repeat myself again, .."))
    assert someEmptyLibrary.countBooks() == 1
    someEmptyLibrary.storeBook(Book("asdfe", "Let me repeat myself again, .."), True)
    assert someEmptyLibrary.countBooks() == 2

def test_library_remove_book(someEmptyLibrary):
    someEmptyLibrary.storeBook(Book("asdfe", "Let me repeat myself, .."))
    assert someEmptyLibrary.countBooks() == 1
    someEmptyLibrary.removeBook("asdf2")
    assert someEmptyLibrary.countBooks() == 1
    someEmptyLibrary.removeBook("asdfe")
    assert someEmptyLibrary.countBooks() == 0

def test_library_get_catalog(someEmptyLibrary, someLargeLibrary):
    # first, test small library
    reportedCatalog = someEmptyLibrary.getCatalog()
    assert len(reportedCatalog) == 0

    someEmptyLibrary.storeBook(Book("asdfe", "Let me repeat myself, .."))
    reportedCatalog = someEmptyLibrary.getCatalog()
    assert len(reportedCatalog) == 1
    assert reportedCatalog[0] == "asdfe"

    # second, large library
    reportedCatalog = someLargeLibrary.getCatalog()
    assert len(reportedCatalog) == someLargeLibrary.countBooks()
    for id in reportedCatalog:
        assert not someLargeLibrary.getBook(id) is None

def test_library_sort_catalog(someLargeLibrary):
    reportedCatalog = someLargeLibrary.sortBooks().getCatalog()
    for i in range(len(reportedCatalog)-1):
        assert reportedCatalog[i] < reportedCatalog[i+1]

def test_library_get_catalog_mocked(someEmptyLibrary):
    someEmptyLibrary.storeBook(Book("tgdi1", "The Great Debate, Issue 1"))
    someEmptyLibrary.storeBook(Book("tgdi2", "The Great Debate, Issue 2"))
    someEmptyLibrary.storeBook(Book("tgdi3", "The Great Debate, Issue 3"))
    # prepare mock
    def getCatalog_mocked():
        return ["tgdi1", "tgdi2", "tgdi3"]

    someEmptyLibrary.getCatalog = Mock(side_effect=getCatalog_mocked)
    
    reportedCatalog = someEmptyLibrary.getCatalog()
    assert len(reportedCatalog) == someEmptyLibrary.countBooks()
    for id in reportedCatalog:
        assert not someEmptyLibrary.getBook(id) is None