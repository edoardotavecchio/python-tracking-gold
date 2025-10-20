from fastapi import FastAPI 
from pydantic import BaseModel
import src.repositories.alpha_vantage as stock_repository

app = FastAPI()

@app.get('/search')
def search(q: str):
    return stock_repository.search(q)

@app.get('/intraday')
def track(symbol: str):
    return stock_repository.intraday(symbol)

@app.get('/quote')
def quote(symbol: str):
    return stock_repository.quote(symbol)