"""simple class to collect books (see book.py) in a list
"""

from book import Book

class Library:
    def __init__(self):
        self.catalog = []

    def storeBook(self, someBook, storeByHigherOrder = False):
        """This method adds someBook to the catalog of the library. 
        If an entry with the same ID already exists, it is only added for storeByHigherOrder == True"""
        if not type(someBook) == Book:
            raise TypeError
        if someBook.id == "":
            raise ValueError

        if not storeByHigherOrder:
            gotBook = self.getBook(someBook.id)
            if gotBook is None:
                self.catalog.append(someBook)
        else:
            self.catalog.append(someBook)

    def countBooks(self):
        return len(self.catalog)

    def removeBook(self, someBookID):
        theBook = self.getBook(someBookID)
        if not theBook is None:
            self.catalog.remove(theBook)

    def getBook(self, someBookID):
        theBook = next((x for x in self.catalog if x.id == someBookID), None)
        return theBook

    def getCatalog(self):
        return [book.id for book in self.catalog]

    def sortBooks(self):
        self.catalog = sorted(self.catalog, key=lambda x: x.id)
        return self
