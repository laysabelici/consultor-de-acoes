import requests
import pandas as pd
from utils.chave_api import chave


def buscar_cotacao(acao):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={acao}&apikey={chave()}'
    r = requests.get(url)
    data = r.json()

    if 'Weekly Time Series' in data:
        df = pd.DataFrame.from_dict(data['Weekly Time Series'], orient='index')
        df.index = pd.to_datetime(df.index)
        return df.head(1)[["1. open", "2. high", "3. low", "4. close", "5. volume"]]
    else:
        return None
