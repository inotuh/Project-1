from modules.library_item import library_item

class Dvd(library_item):
    def __init__(self, title, upc, subject, actors, directors, genre):
        super().__init__(title, upc, subject)
        self.actors = actors
        self.directors = directors
        self.genre = genre