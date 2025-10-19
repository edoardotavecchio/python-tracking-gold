import requests
import urllib

(scheme, netloc, path) = 'https', 'www.alphavantage.co', 'query'
apikey = 'KZXWK2KBEPUALTGO'

def intraday(symbol: str):
    function='TIME_SERIES_INTRADAY'
    interval='60min'
    query_parts = (
        ('function', function),
        ('symbol', symbol),
        ('interval', interval),
        ('apikey', apikey)
    )
    query =  urllib.parse.urlencode(query_parts)
    url_parts = (scheme, netloc, path, query, fragment:=None)
    url = urllib.parse.urlunsplit(url_parts)
    r = requests.get(url)
    return r.json()