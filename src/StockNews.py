# News Sentiment Analysis using Python, Pandas, and BeautifulSoup
# Takes in article data from the FMP financial information endpoint and gathers the sentiment through
# polarity and subjectivity calculations. Determines whether these articles were based on facts or opinions

def FMPNews(page=0, size=5):
    key = 'jvL9q2IaEmqL48PgKjBPShfwhIBBeOj2'
    return f'https://financialmodelingprep.com/api/v3/fmp/articles?page={page}&size={size}&apikey={key}'

import requests
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
import time 

# Display all rows
pd.set_option('display.max_rows', None)

# Display all columns
pd.set_option('display.max_columns', None)


def GatherSentiment(lowerPOL, upperPOL, lowerSBJ, upperSBJ):
    def HandleSentiment(f):
        def SolveForIt(*a, **b):
            data = f(*a, **b)
            stocks = list(data.keys())
            result = {stk:{'positive':0,'negative':0,'opinion':0,'fact':0} for stk in stocks}
            for ticker, paragraph in data.items():
                for sentence in paragraph:
                    ML = TextBlob(sentence).sentiment
                    POL = ML.polarity
                    SBJ = ML.subjectivity
                    if POL >= upperPOL:
                        result[ticker]['positive'] += 1
                    elif POL <= lowerPOL:
                        result[ticker]['negative'] += 1
                    else:
                        pass
                    if SBJ >= upperSBJ:
                        result[ticker]['fact'] += 1
                    elif SBJ <= lowerSBJ:
                        result[ticker]['opinion'] += 1
            return result
        return SolveForIt
    return HandleSentiment

def ExtractFromHTML(f):
    def ProblemSolution(*a, **b):
        tickers, stocks, result = f(*a, **b)
        data = {stk:[] for stk in stocks}
        for stock, article in zip(stocks, result):
            soup = BeautifulSoup(article, 'html.parser')
            data[stock] += [u.get_text() for u in soup.find_all('p')]
        return data
    return ProblemSolution

def CreateDataFrame(f):
    def Solve(*a, **b):
        z = f(*a, **b)
        final_result = []
        stocks = list(z.keys())
        for i in stocks:
            final_result.append(z[i])
        df = pd.DataFrame(final_result, index=stocks)
        return df
    return Solve

@CreateDataFrame
@GatherSentiment(-0.45, 0.45, 0.2, 0.8)
@ExtractFromHTML
def FetchData(pages, size):
    def CutTicks(x):
        if ':' in x:
            x = x.split(':')[1]
            return x
        return x
    result = []
    stocks = []
    for page in range(pages):
        print("Fetching page number ", page)
        url = FMPNews(page=page, size=size)
        resp = requests.get(url).json()
        resp = resp['content']
        stocks += [CutTicks(t['tickers']) for t in resp]
        result += [t['content'] for t in resp]
        time.sleep(0.7)
    tickers = list(set(stocks))
    return tickers, stocks, result

pages = 1
size = 500

sentiment = FetchData(pages, size)

sentiment = sentiment.sort_values(by='positive', ascending=False)
print(sentiment)

import matplotlib.pyplot as plt

x = sentiment['opinion'].values
y = sentiment['fact'].values

plt.scatter(x, y, color='red')
plt.show()
