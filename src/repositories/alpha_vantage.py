import requests
import urllib

(scheme, netloc, path) = 'https', 'www.alphavantage.co', 'query'
apikey = 'KZXWK2KBEPUALTGO'

def intraday(symbol: str):
    parts = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '60min',
        'apikey': apikey,
    }

    query =  urllib.parse.urlencode(parts)

    url_parts = (scheme, netloc, path, query, fragment:=None)
    url = urllib.parse.urlunsplit(url_parts)

    r = requests.get(url)
    return r.json()

def search(query: str):
    parts = {
        'function': 'SYMBOL_SEARCH',
        'keywords': query,
        'apikey': apikey,
    }
    query = urllib.parse.urlencode(parts)

    url_parts = (scheme, netloc, path, query, fragment:=None)
    url = urllib.parse.urlunsplit(url_parts)

    r = requests.get(url)
    return r.json()

def quote(symbol: str):
    parts = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': apikey,
    }
    query = urllib.parse.urlencode(parts)

    url_parts = (scheme, netloc, path, query, fragment:=None)
    url = urllib.parse.urlunsplit(url_parts)

    r = requests.get(url)
    return r.json()
