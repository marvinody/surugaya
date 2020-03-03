import re
from enum import Enum
from math import ceil

import requests
from bs4 import BeautifulSoup

rootURL = "https://www.suruga-ya.jp/search?category=&=gift+closet"

availabilityMap = {
    '新品': 'Brand New',
    '中古': 'Second Hand',
    '定価': 'List Price',
    '予約': 'Preorder',
}


class Item:
    def __init__(self, *args, **kwargs):
        self.productURL = kwargs['productURL']
        self.imageURL = kwargs['imageURL']
        self.productName = kwargs['productName']
        self.price = kwargs['price']
        self.productCode = kwargs['productCode']
        self.availability = kwargs['availability']


def createItem(url, name, priceLine):
    # this will pull a bunch of junk with it like yen sign and weird chars
    priceText = priceLine.text
    # so we just remove anything that's not a digit
    priceDigits = re.sub('[^0-9]', '', priceText)
    # and just parse into int
    price = int(priceDigits)

    availabilityJP = re.search('(.*)：', priceText).group(1).strip()
    productCode=url[url.rindex("/")+1:]
    return Item(
        productURL=url,
        imageURL=getImageUrl(productCode),
        productName=name,
        price=price,
        productCode=productCode,
        availability=availabilityMap[availabilityJP],
    )
def getImageUrl(productCode):
    return 'https://www.suruga-ya.jp/pics/boxart_m/{}m.jpg'.format(productCode)

def createItems(productHTML):
    productURL = productHTML.find('a')['href']
    productName = productHTML.find('p', class_='title').text
    return [createItem(productURL, productName, priceLine) for priceLine in productHTML.find_all('p', class_='price_teika')]


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
        yield from [createdItem for item in items for createdItem in createItems(item)]
        data['page'] += 1
        items = parse(rootURL, data)
