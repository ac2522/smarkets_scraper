import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
result = requests.get("https://smarkets.com/event/886716/politics/uk/uk-party-leaders/next-conservative-leader")
src = result.content
soup = BeautifulSoup(src, 'xml')
atv = soup.find_all('div',{'class':"contract open"})
for e in atv:
    arb = e.find(class_ = "name")
    name_ = arb.find(class_ = "formatted-content")
    price = e.find(class_="price tick buy   formatted-price numeric-value")
    price2 = e.find(class_="price tick sell   formatted-price numeric-value")
    if price == None: p = "No liquidity"
    else: p = price.string
    if price2 == None: p2 = "No liquidity"
    else: p2 = price2.string
    print(name_.string, "  buy:", p, "  sell:", p2)
    print()
