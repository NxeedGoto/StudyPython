import requests
from bs4 import BeautifulSoup


res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
BookClasses = soup.find_all(class_='product_pod')
for BookClass in BookClasses:
    BookNamePs = BookClass.find_all(name='h3')
    for BookNameP in BookNamePs:
        BookName = BookNameP.find(attrs={'title': True}).get('title')
        print(BookName)
    BookRatings = BookClass.find_all(name='p', class_='star-rating')
    for BookRatings in BookRatings:
        print(BookRatings['class'][1])
    BookPriceClasses = BookClass.find_all(name='div', class_='product_price')
    for BookPriceClass in BookPriceClasses:
        BookPrices = BookPriceClass.find_all(name='p', class_='price_color')
        for BookPrice in BookPrices:
            print(BookPrice.text)
input()