def FMPNews(page = 1, size = 5):
    key = 'jvL9q2IaEmqL48PgKjBPShfwhIBBeOj2'
    return f'https://financialmodelingprep.com/api/v3/fmp/articles?page={page}&size={size}&apikey={key}'

import requests
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# display all rows
pd.set_option('display.max_rows', None)

# display all columns
pd.set_option('display.max_columns', None)

# first decorator function
def ExtractFromHTML(f):
    def ProblemSolution(*a, **b):
        tickers, stocks, result = f(*a, **b)
        data = {}
        for stock, article in zip(stocks, result):
            soup = BeautifulSoup(article, 'html.parser')
            data[stock] = [u.get_text() for u in soup.find_all('p')]
        return data
    return ProblemSolution

            
@ExtractFromHTML
def getData(pages, size):
    def cutTickers(x):
        if ':' in x:
            x = x.split(':')[1]
            return x
        return x
    result = []
    stocks = []
    for page in range(pages): 
        print("Fetching page number ", page)
        req = FMPNews(page=page, size=size)
        response = requests.get(req).json()
        response = response['content']
        stocks += [cutTickers(t['content']) for t in response]
        result += [t['content'] for t in response]
    tickers = list(set(stocks))
    return tickers, stocks, result
        
pages = 1
size = 2

for i, j in getData(pages, size).items():
    print(i, len(j))
    

