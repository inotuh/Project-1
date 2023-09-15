from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog
import json

f = open('./modules/files/data.json')
data_json = json.load(f)

list_book = []
list_magazine = []
list_dvd = []
list_cd = []

for item in data_json:
    if item['source'] == 'book':
        list_book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title=item ['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']    
        ))
    elif item['source']  =='dvd':
        list_dvd.append(Dvd(
            title=item ['title'],
            subject=item ['subject'],
            upc=item ['upc'],
            actors=item ['actors'],
            directors=item ['directors'],
            genre=item ['genre']
        ))
    elif item['source'] == 'cd':
        list_cd.append(Cd(
            title=item ['title'],
            subject=item ['subject'],
            upc=item ['upc'],
            artist=item ['artist']
        ))

Catalog_all =[list_book, list_magazine, list_dvd, list_cd]    

input_search = 'media_cnn'
result = Catalog(Catalog_all).search(input_search)

print('=====| result |=====')
for index, result in enumerate(result):
    print(f'result ke-{index+1} | {result}')


