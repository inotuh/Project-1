from modules.library_item import library_item



class Book():
    def __init__(self, isbn, authors, title, subject, dds_number, upc):
        library_item.__init__(self, title, upc, subject)
        self.isbn = isbn
        self.authors = authors
        self.dds_number = dds_number
       