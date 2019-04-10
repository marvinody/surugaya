import requests
import re

from bs4 import BeautifulSoup
from math import ceil
from enum import Enum

rootURL = "https://www.suruga-ya.jp/search?category=&=gift+closet"

availabilityMap = {
    '新品': 'Brand New',
    '中古': 'Second Hand',
}


class Item:
    def __init__(self, *args, **kwargs):
        self.productURL = kwargs['productURL']
        self.imageURL = kwargs['imageURL']
        self.productName = kwargs['productName']
        self.price = kwargs['price']
        self.productCode = kwargs['productCode']
        self.availability = kwargs['availability']


def createItem(productHTML):
    productURL = productHTML.find('a')['href']
    # this will pull a bunch of junk with it like yen sign and weird chars
    priceText = productHTML.find('p', class_='price').text
    # so we just remove anything that's not a digit
    priceDigits = re.sub('[^0123456789]', '', priceText)
    # and just parse into int
    price = int(priceDigits)
    availabilityJP = productHTML.find('p', class_='condition').find('span').text
    item = Item(
        productURL=productURL,
        imageURL=productHTML.find('img')['src'],
        productName=productHTML.find('p', class_='title').text,
        price=price,
        productCode=productURL[productURL.rindex("/")+1:],
        availability=availabilityMap[availabilityJP],
    )
    return item

def parse(url, data):
    # returns [] if page has no items on it
    # returns [Item's] otherwise
    r = requests.get(url, data)
    html = BeautifulSoup(r.text, "html.parser")
    return html.find_all("div", class_="item")

def search(keywords):
    data = {
        "search_word": keywords,
        "page": 1,
    }

    items = parse(rootURL, data)
    while items:
        yield from [createItem(item) for item in items]
        data['page'] += 1
        items = parse(rootURL, data)
