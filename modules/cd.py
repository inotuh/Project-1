from modules.library_item import library_item

class Cd(library_item):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)
        self.artist = artist