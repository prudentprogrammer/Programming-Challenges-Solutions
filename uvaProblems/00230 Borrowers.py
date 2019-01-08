# Link: https://uva.onlinejudge.org/external/2/230.pdf

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.returned = False
        self.borrowed = False

    def __repr__(self):
        return "({}, {}, {}, {})".format(self.title,
                                        self.author,
                                        self.returned,
                                        self.borrowed)

def processQueries(queries, books):
    for query in queries:
        currLine = query.split(" ", 1)
        cmd, bookName = currLine[0], currLine[-1][1:-1]

        if cmd == "BORROW":
            for currBook in books:
                if currBook.title == bookName:
                    currBook.borrowed = True

        elif cmd == "RETURN":
            for currBook in books:
                if currBook.title == bookName:
                    currBook.returned = True

        elif cmd == "SHELVE":
            prevBook = None
            for currBook in books:
                if not currBook.borrowed:
                    prevBook = currBook
                elif currBook.returned:
                    if not prevBook:
                        print("Put \"{}\" first".format(currBook.title))
                    else:
                        print("Put \"{}\" after \"{}\"".format(currBook.title, prevBook.title))
                    currBook.returned = False
                    currBook.borrowed = False
                    prevBook = currBook
            print("END")

if __name__ == "__main__":
    books = []
    while True:
        currentLine = input()
        if currentLine == "END": break

        # Get indices of the double quotes to extract the book name
        firstIndex = currentLine.index("\"")
        secondIndex = currentLine.index("\"", firstIndex + 1)

        title = currentLine[firstIndex + 1: secondIndex]
        author = currentLine[currentLine.index("by") + 3:]
        book = Book(title, author)
        books.append(book)

    # Sort the books by author first and then the book title
    books.sort(key=lambda book:(book.author, book.title))

    queries = []
    while True:
        query = input()
        if query == "END": break
        queries.append(query)

    processQueries(queries, books)
