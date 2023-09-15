from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd

class Catalog():
    def __init__(self, catalog=None):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search.lower() in item.title.lower():
                    if type(item) == Book:
                        list_result.append(f'title : {item.title}, type catalog: book')
                    elif type(item) == Magazine:
                        list_result.append(f'title : {item.title}, type catalog: magazine')
                    elif type(item) == Dvd:
                        list_result.append(f'title : {item.title}, type catalog: dvd')
                    elif type(item) == Cd:
                        list_result.append(f'title : {item.title}, type catalog: cd')
                    else:
                        pass
        return list_result
 